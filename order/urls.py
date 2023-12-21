from django.urls import path
from order import views

urlpatterns = [
    path("buy/<int:pk>", views.ItemBuyApiView.as_view(), name="item-buy"),
    path("item/<int:pk>", views.ItemDetailView.as_view(), name="item-detail"),

    path("buy-order/<int:pk>", views.OrderBuyApiView.as_view(), name="order-buy"),
    path("order/<int:pk>", views.OrderDetailView.as_view(), name="order-detail"),
]
