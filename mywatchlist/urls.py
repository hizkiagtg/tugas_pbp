from django.urls import path
from mywatchlist.views import *

app_name = 'mywatchlist'

urlpatterns = [
    path('html/', show_watchlist, name='show_watchlist'),
    path('<str:jenis>/', show, name = "show"),
]