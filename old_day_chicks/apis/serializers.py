from rest_framework import serializers
from old_day_chicks.models import DayOldChicksOrder


class DayOldChicksOrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = DayOldChicksOrder
        fields = (
            "firstName",
            "lastName",
            "location",
            "layers",
            "broilers",
            "numberOfBirds",
            "kenbros",
            "message",
        )
