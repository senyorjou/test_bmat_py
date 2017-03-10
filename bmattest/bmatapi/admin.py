from django.contrib import admin

# Register your models here.
from .models import Channel, Performer, Play, Song


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name', )


@admin.register(Performer)
class PerformerAdmin(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name', )


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    fields = ('title', 'performer', 'length')
    list_display = ('title', 'performer', 'length')


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    fields = ('channel', 'title', 'performer', 'start')
    list_display = ('channel', 'title', 'performer', 'start')
