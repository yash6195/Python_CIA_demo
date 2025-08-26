# backend/seed.py
import os
import django
import random
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from core.models import Product, Task, Order, User  # adjust imports if models are in different app

# Only seed if no data exists
if not Product.objects.exists():
    print("Seeding demo data...")

    # Create demo products
    products = [
        Product(name="Laptop", price=1200, stock=10),
        Product(name="Headphones", price=150, stock=50),
        Product(name="Smartphone", price=800, stock=20),
    ]
    Product.objects.bulk_create(products)

    # Create demo users
    users = [
        User(username="alice", email="alice@example.com", gender="Female"),
        User(username="bob", email="bob@example.com", gender="Male"),
    ]
    User.objects.bulk_create(users)

    # Create demo tasks
    tasks = [
        Task(title="Check inventory", description="Weekly stock check"),
        Task(title="Process orders", description="Handle pending shipments"),
    ]
    Task.objects.bulk_create(tasks)


    print("✅ Seeding completed.")
else:
    print("Data already exists, skipping seeding.")

