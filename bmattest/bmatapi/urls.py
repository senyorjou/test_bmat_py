"""
API urls
"""
from django.conf.urls import url

from .views import ChannelView, PerformerView, PlayView, SongView
from .views import GetChannelPlays, GetSongPlays, GetTop

urlpatterns = [
    url(r'^add_channel$', ChannelView.as_view(), name='channels_api_view'),
    url(r'^add_performer$', PerformerView.as_view(),
        name='performer_api_view'),
    url(r'^add_song$', SongView.as_view(), name='song_api_view'),
    url(r'^add_play$', PlayView.as_view(), name='play_api_view'),
    url(r'^get_channel_plays$', GetChannelPlays.as_view(),
        name='get_channels_api_view'),
    url(r'^get_song_plays$', GetSongPlays.as_view(),
        name='get_songs_api_view'),
    url(r'^get_top$', GetTop.as_view(),
        name='get_top_api_view'),
]
