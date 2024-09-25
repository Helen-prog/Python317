from django.urls import path
from order.views import OrderCreateView, full_order

urlpatterns = [
    path("order-create/", OrderCreateView.as_view(), name="order-create"),
    path("full-order/", full_order, name="full-order"),
]
