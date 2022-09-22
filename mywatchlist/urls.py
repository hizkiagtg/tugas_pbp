from django.urls import path
from mywatchlist.views import *

app_name = 'mywatchlist'

urlpatterns = [
    path('html/', show_watchlist, name='show_watchlist'),
    path('xml/', show_xml, name= 'show_xml'), 
    path('json/', show_json, name='show_json'),
]