from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index , name="index"),
    path('api/note', views.getNotes , name="note"),
    path('api/note/<str:title>', views.modify_notes , name="add/delete_note")
    # path('api', views.getData , name="api"),
    # path('post', views.postData , name="post"),
    # path('getUserData/<str:user_name>', views.getUserData , name="user_data")

]
