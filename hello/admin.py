from django.contrib import admin
from .models import Video, Comment
# from django.contrib.auth import get_user_model


# User = get_user_model()


class VideoInLine(admin.StackedInline):  # указывает связь
    model = Comment
    extra = 2  # Количество коментариев под статьей


class VideoAdmin(admin.ModelAdmin):
    inlines = [VideoInLine]
    list_filter = ['Video_data']


admin.site.register(Video, VideoAdmin)
# admin.site.register(User)
# admin.site.unregister(User)

# Register your models here.
