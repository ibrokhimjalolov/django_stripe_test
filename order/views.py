from typing import Any
from django.views.generic import DetailView
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from order import models
from order import service as order_service


class ItemBuyApiView(APIView):
    
    def get(self, request, pk):
        item = get_object_or_404(models.Item, pk=pk)
        session_id = order_service.get_item_stripe_session(item)
        return Response({"session_id": session_id})


class ItemDetailView(DetailView):
    queryset = models.Item.objects.all()

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cnt["stripe_publishable_key"] = settings.STRIPE_PUBLISHABLE_KEY
        return cnt
