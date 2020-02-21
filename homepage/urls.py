from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('clue/<int:pk>/', views.clue_detail, name='clue_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('clue/new/', views.clue_new, name='clue_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('clue/<int:pk>/edit/', views.clue_edit, name='clue_edit')
    
]
