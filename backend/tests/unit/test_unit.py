import pytest
from django.contrib.auth.models import User
from base.models import Product, Review, Order, OrderItem, ShippingAddress


@pytest.mark.django_db
def test_product_model():
    user = User.objects.create_user(username="testuser", password="testpass")
    product = Product.objects.create(
        user=user,
        name="Test Product",
        brand="Test Brand",
        price=100.00,
    )
    assert product.name == "Test Product"
    assert product.brand == "Test Brand"
    assert str(product) == "Test Product | Test Brand | 100.0"


@pytest.mark.django_db
def test_review_model():
    user = User.objects.create_user(username="testuser", password="testpass")
    product = Product.objects.create(name="Test Product")
    review = Review.objects.create(
        product=product, user=user, name="Test Review", rating=5, comment="Excellent!"
    )
    assert review.rating == 5
    assert review.comment == "Excellent!"
    assert str(review) == "5"


@pytest.mark.django_db
def test_order_model():
    user = User.objects.create_user(username="testuser", password="testpass")
    order = Order.objects.create(
        user=user, paymentMethod="Credit Card", totalPrice=200.00
    )
    assert order.paymentMethod == "Credit Card"
    assert order.totalPrice == 200.00
    assert str(order) == str(order.createdAt)


@pytest.mark.django_db
def test_order_item_model():
    product = Product.objects.create(name="Test Product")
    order = Order.objects.create()
    order_item = OrderItem.objects.create(
        product=product, order=order, name="Test Item", qty=2, price=50.00
    )
    assert order_item.qty == 2
    assert order_item.price == 50.00
    assert str(order_item) == "Test Item"


@pytest.mark.django_db
def test_shipping_address_model():
    order = Order.objects.create()
    address = ShippingAddress.objects.create(
        order=order, address="123 Main St", city="Test City", postalCode="12345"
    )
    assert address.city == "Test City"
    assert address.postalCode == "12345"
    assert str(address) == "123 Main St"
