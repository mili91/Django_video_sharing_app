from django.shortcuts import render
from .models import Video


def index(request):
    return render(request, 'video/index.html')

def video(request, video_id):
    the_video = Video.objects.get(pk=video_id)
    context = {'the_video' : the_video}
    return render(request, 'video/video.html', context)