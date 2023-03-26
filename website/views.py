from django.shortcuts import render
from .models import Song

# Create your views here.
def index(request):
    songs = Song.objects.filter().all()
    return render(request, 'website/index.html',{'songs':songs})