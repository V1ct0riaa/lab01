from django.urls import path
from wishlist.views import show_dataxml, show_wishlist
from wishlist.views import show_dataxml
from wishlist.views import show_datajson
from wishlist.views import show_json_by_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_dataxml, name='show_dataxml'),
    path('json/', show_datajson, name='show_datajson'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
]