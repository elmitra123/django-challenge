from rest_framework import serializers
from .models import Stadium, Seat, Match


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = ('name',)


class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = ('id', 'firstteamname', 'secondteamname', 'date', 'stadium',)


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ('id', 'number', 'match', )



