from rest_framework import serializers

from .models import Channel, Performer, Play, Song


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'


class PerformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performer
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'performer', 'length')


class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = '__all__'


class GetChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ('performer', 'title', 'start', 'end')
