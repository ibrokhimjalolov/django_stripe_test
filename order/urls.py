from django.urls import path
from order import views

urlpatterns = [
    path("buy/<int:pk>", views.ItemBuyApiView.as_view(), name="item-buy"),
    path("item/<int:pk>", views.ItemDetailView.as_view(), name="item-detail"),
]
