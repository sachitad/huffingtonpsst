from django import template

from video.models import Video, VideoComment

register = template.Library()


@register.filter()
def get_video_id(youtube_url):
    try:
        return youtube_url.rsplit('?v=')[1]
    except IndexError:
        pass


@register.assignment_tag()
def get_video_comments():
    return VideoComment.objects.all()


@register.assignment_tag()
def get_videos():
    return Video.objects.filter(live=True).order_by('-created')[:6]


@register.assignment_tag()
def get_videos_couch():
    return Video.objects.filter(live=True, tags__name='couch').order_by('-created')[:10]