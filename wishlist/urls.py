from django.urls import path
from wishlist.views import show_dataxml, show_json_by_id_xml, show_wishlist,show_json_by_id,show_datajson


app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_dataxml, name='show_dataxml'),
    path('json/', show_datajson, name='show_datajson'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_json_by_id_xml, name='show_json_by_id_xml'),
]