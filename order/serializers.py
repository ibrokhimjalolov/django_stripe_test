from rest_framework import serializers
from order import models


class BuyItemResponseSerializer(serializers.Serializer):
    session_id = serializers.CharField()
