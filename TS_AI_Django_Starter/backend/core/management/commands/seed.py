from django.core.management.base import BaseCommand
from core.models import Product, Task, Order, User
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = "Seed the database with demo data"

    def handle(self, *args, **kwargs):
        if Product.objects.exists():
            self.stdout.write(self.style.WARNING("Data already exists, skipping seeding."))
            return

        self.stdout.write("Seeding demo data...")

        # Create demo products
        products = [
            Product(name="Laptop", price=1200, stock=10),
            Product(name="Headphones", price=150, stock=50),
            Product(name="Smartphone", price=800, stock=20),
        ]
        Product.objects.bulk_create(products)

        # Create demo users
        users = [
            User(username="alice", email="alice@example.com"),
            User(username="bob", email="bob@example.com"),
        ]
        User.objects.bulk_create(users)

        # Create demo tasks
        tasks = [
            Task(title="Check inventory", description="Weekly stock check"),
            Task(title="Process orders", description="Handle pending shipments"),
        ]
        Task.objects.bulk_create(tasks)

        # Create demo orders
        for _ in range(10):
            Order.objects.create(
                product=random.choice(Product.objects.all()),
                quantity=random.randint(1, 5),
                order_date=datetime.now() - timedelta(days=random.randint(0, 30))
            )

        self.stdout.write(self.style.SUCCESS("✅ Seeding completed."))

