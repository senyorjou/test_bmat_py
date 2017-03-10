"""
API urls
"""
from django.conf.urls import url

from .views import ChannelView, PerformerView, PlayView, SongView

urlpatterns = [
    url(r'^add_channel$', ChannelView.as_view(), name='channels_api_view'),
    url(r'^add_performer$', PerformerView.as_view(),
        name='performer_api_view'),
    url(r'^add_song$', SongView.as_view(), name='song_api_view'),
    url(r'^add_play$', PlayView.as_view(), name='play_api_view'),
    # url(r'^get_channel_plays$', PlayView.as_view(), name='play_api_view'),
]
