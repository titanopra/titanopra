from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from .models import Media,Detail_media
# Create your views here.
def home(request):
    medias = Media.objects.all()
    return render(request, 'novin_media/media.html', {'medias': medias})

def detail(request,pk):
    media = Media.objects.get(id=pk)
    mediaa = Detail_media.objects.filter(id=pk)
    detail_media = Detail_media.objects.all()
    return render(request, 'novin_media/media-details.html',{'pk':media,'detail_media':detail_media,'mediaa':mediaa})