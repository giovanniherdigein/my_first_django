from django.urls import path
from . import views

app_name ='crudsite'
urlpatterns=[
    path('',views.index,name='index'),
    path('create_item',views.createItem,name= 'create_item'),
    path('update_item/<int:item_id>/',views.updateItem,name='update_item'),
path('delete_item/<int:item_id>/',views.deleteItem,name='delete_item'),
]