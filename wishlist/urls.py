from django.urls import path
from wishlist.views import show_dataxml, show_json_by_id_xml, show_wishlist,show_json_by_id,show_datajson,register,login_user,logout_user


app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('html', show_wishlist, name='show_wishlist'),
    path('xml/', show_dataxml, name='show_dataxml'),
    path('json/', show_datajson, name='show_datajson'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_json_by_id_xml, name='show_json_by_id_xml'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

]