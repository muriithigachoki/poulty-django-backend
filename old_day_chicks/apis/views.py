from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from old_day_chicks.models import DayOldChicksOrder
from old_day_chicks.apis.serializers import DayOldChicksOrderSerializers


class DayOldChicksOrderListAPIView(ListCreateAPIView):
    queryset = DayOldChicksOrder.objects.all()
    serializer_class = DayOldChicksOrderSerializers


class DayOldChicksOrderDetailsAPIView(RetrieveUpdateDestroyAPIView):
    queryset = DayOldChicksOrder.objects.all()
    serializer_class = DayOldChicksOrderSerializers
