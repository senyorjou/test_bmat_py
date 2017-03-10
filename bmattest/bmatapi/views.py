# from django.shortcuts import render
# from rest_framework import generics
# from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# from .models import Channel, Performer, Song
from .serializers import ChannelSerializer, PerformerSerializer,\
                         PlaySerializer, SongSerializer


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
