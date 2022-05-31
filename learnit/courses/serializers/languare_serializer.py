from rest_framework import serializers

from courses.models import Languare


class LanguareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languare
        fields = ["id", "name", "priority"]
