from rest_framework import serializers

from models import Plays


class PlaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plays
        fields = ['title', 'date', 'logo', 'duration', 'age_limit', 'pushkins_card', 'annotation']
