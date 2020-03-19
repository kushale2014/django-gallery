from django.shortcuts import render
from django.http import Http404
from .models import Album
from django.core.paginator import Paginator
from os import listdir

# // кол-во фото на страницу
perpage = 3

def index(request):
    list_albums = Album.objects.all().order_by("title")
    return render(request, 'list.html', {'list_albums' : list_albums})

def detail(request, album_id):
    try:
        a = Album.objects.get( id = album_id )
    except:
        raise Http404('Альбом не найден!!!')

    paginator = Paginator(a.image_set.all(), perpage)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'detail_ajax.html' if request.is_ajax() else 'detail.html',
                        {'a': a, 
                        'page_obj' : page_obj,
                        })

def get_images():
    files = listdir(path=MEDIA_ROOT)
    if files.count == 0:
        return False
    pattern = "#\.(jpe?g|png|gif)$#i"
