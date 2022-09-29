from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from mywatchlist.models import MyWatchList

def show_watchlist(request):
    data = MyWatchList.objects.all()
    watched = 0
    not_watched = 0
    message = ""
    for watchlist in data:
        if (watchlist.watched):
            watched += 1
        else:
            not_watched += 1
    if (watched >= not_watched):
        message += "Selamat, kamu sudah banyak menonton!"
    else:
        message += "Wah, kamu masih sedikit menonton!"
    context = {
        'list_watchlist': data,
        'nama': 'Hizkia Sebastian Ginting',
        'npm' : '2106750881',
        'project_name' : 'TUGAS 3 PBP',
        'message': message
    }
    return render(request, "mywatchlist.html", context)

def show(request, jenis):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize(jenis, data), content_type="application/" + jenis)
