from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db.models import Q, Avg, Count
from .models import Product, Task, Order
from .serializers import UserSerializer, ProductSerializer, TaskSerializer, OrderSerializer
from .utils import random_value, simulate_delay

class BulkCreateMixin:
    @action(detail=False, methods=['post'])
    def bulk_create(self, request):
        many = isinstance(request.data, list)
        if not many:
            return Response({"detail": "Expected a list for bulk_create"}, status=400)
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        objs = [self.queryset.model(**item) for item in serializer.validated_data]
        self.queryset.model.objects.bulk_create(objs)
        return Response({"status": "bulk insert success", "count": len(objs)}, status=201)

class UserViewSet(BulkCreateMixin, viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-id")
    serializer_class = UserSerializer
    filterset_fields = ["is_active"]
    search_fields = ["username", "email"]

class ProductViewSet(BulkCreateMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("-id")
    serializer_class = ProductSerializer
    filterset_fields = ["category"]
    search_fields = ["name", "category"]

    def list(self, request, *args, **kwargs):
        qs = self.queryset
        min_price = request.GET.get("minPrice")
        max_price = request.GET.get("maxPrice")
        sort = request.GET.get("sort")
        if min_price:
            qs = qs.filter(price__gte=min_price)
        if max_price:
            qs = qs.filter(price__lte=max_price)
        if sort == "price_asc":
            qs = qs.order_by("price")
        elif sort == "price_desc":
            qs = qs.order_by("-price")
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

class TaskViewSet(BulkCreateMixin, viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("-id")
    serializer_class = TaskSerializer
    filterset_fields = ["priority", "completed", "assigned_to"]

class OrderViewSet(BulkCreateMixin, viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by("-id")
    serializer_class = OrderSerializer
    filterset_fields = ["status", "user", "product"]

@api_view(["GET"])
def health(request):
    return Response({
        "status": "ok",
        "counts": {
            "users": User.objects.count(),
            "products": Product.objects.count(),
            "tasks": Task.objects.count(),
            "orders": Order.objects.count(),
        }
    })

@api_view(["GET"])
def analytics(request):
    return Response({
        "users": User.objects.count(),
        "products": Product.objects.count(),
        "orders": Order.objects.count(),
        "avg_price": Product.objects.aggregate(avg=Avg("price"))["avg"],
        "tasks_completed": Task.objects.filter(completed=True).count(),
    })

@api_view(["GET"])
def search(request):
    q = request.GET.get("q", "")
    results = {
        "users": list(User.objects.filter(Q(username__icontains=q) | Q(email__icontains=q)).values("id","username","email")),
        "products": list(Product.objects.filter(Q(name__icontains=q) | Q(category__icontains=q)).values()),
        "tasks": list(Task.objects.filter(Q(title__icontains=q) | Q(description__icontains=q)).values()),
        "orders": list(Order.objects.filter(Q(status__icontains=q)).values()),
    }
    return Response(results)

@api_view(["GET"])
def test_slow(request):
    delay = int(request.GET.get("delay", "1000"))
    simulate_delay(delay)
    return Response({"delayed_ms": delay})

@api_view(["GET"])
def test_error(request, code: int):
    return Response({"message": f"Simulated error {code}"}, status=code)

@api_view(["POST"])
def test_echo(request):
    return Response({"echo": request.data})

@api_view(["GET"])
def test_random(request):
    typ = request.GET.get("type", "string")
    return Response({"type": typ, "value": random_value(typ)})
