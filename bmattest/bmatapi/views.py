import ast
from datetime import datetime

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import Play

#  POST serializers
from .serializers import ChannelSerializer, PerformerSerializer,\
                         PlaySerializer, SongSerializer
#  GET serializers
from .serializers import GetChannelSerializer, GetSongSerializer,\
                         GetTopSerializer

DTPATT = '%Y-%m-%dT%H:%M:%S'


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = {}
        response_data['result'] = data
        response_data['code'] = 0

        response = super(CustomJSONRenderer, self).\
            render(response_data, accepted_media_type,
                   renderer_context)

        return response


class ChannelView(APIView):
    def post(self, request, format=None):
        serializer = ChannelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 0,
                'result': serializer.data
            }

            return Response(response, status=status.HTTP_201_CREATED)

        response = {
            'status': 200,
            'errors': ['Resource already in database']
        }

        return Response(response, status=status.HTTP_200_OK)


class PerformerView(APIView):
    def post(self, request, format=None):
        serializer = PerformerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 0,
                'result': serializer.data
            }

            return Response(response, status=status.HTTP_201_CREATED)

        response = {
            'status': 200,
            'errors': ['Resource already in database']
        }

        return Response(response, status=status.HTTP_200_OK)


class SongView(APIView):
    def post(self, request, format=None):
        song_serializer = SongSerializer(data=request.data)

        if song_serializer.is_valid():
            data = {'name': request.data['performer']}
            per_serializer = PerformerSerializer(data=data)

            if per_serializer.is_valid():
                per_serializer.save()

            song_serializer.save()
            response = {
                'status': 0,
                'result': song_serializer.data
            }

            return Response(response, status=status.HTTP_201_CREATED)

        response = {
            'status': 200,
            'errors': ['Resource already in database']
        }

        return Response(response, status=status.HTTP_200_OK)


class PlayView(APIView):
    def post(self, request, format=None):
        serializer = PlaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 0,
                'result': serializer.data
            }

            return Response(response, status=status.HTTP_201_CREATED)

        response = {
            'status': 200,
            'errors': ['Resource already in database']
        }

        return Response(response, status=status.HTTP_200_OK)


class GetChannelPlays(generics.ListAPIView):
    serializer_class = GetChannelSerializer
    renderer_classes = (CustomJSONRenderer, )

    def get_queryset(self):
        channel = self.request.query_params['channel']
        start = datetime.strptime(self.request.query_params['start'], DTPATT)
        end = datetime.strptime(self.request.query_params['end'], DTPATT)

        return Play.objects.filter(channel=channel, start__gte=start,
                                   end__lte=end)


class GetSongPlays(generics.ListAPIView):
    serializer_class = GetSongSerializer
    renderer_classes = (CustomJSONRenderer, )

    def get_queryset(self):
        title = self.request.query_params['title']
        performer = self.request.query_params['performer']
        start = datetime.strptime(self.request.query_params['start'], DTPATT)
        end = datetime.strptime(self.request.query_params['end'], DTPATT)

        return Play.objects.filter(title=title, performer=performer,
                                   start__gte=start, end__lte=end)


class GetTop(generics.ListAPIView):
    serializer_class = GetTopSerializer
    renderer_classes = (CustomJSONRenderer, )

    def get_queryset(self):
        channels = ast.literal_eval(self.request.query_params['channels'])
        print channels, type(channels)
        # limit = self.request.query_params['limit']
        start = datetime.strptime(self.request.query_params['start'], DTPATT)

        return Play.objects.filter(channel__name__in=channels,
                                   start__gte=start)
