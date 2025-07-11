from django.urls import path
from . import views

urlpatterns=[
    path('',views.main,name='main_page'),
    path('books/',views.book_list,name='book_list'),
    path('add/', views.add_book, name='add_book'),


]