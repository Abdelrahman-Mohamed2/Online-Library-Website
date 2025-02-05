from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.get_home_admin, name='home-admin'),
    path('<int:id>', views.get_book_details, name='book-details'),
    path('not-found/', views.get_not_found, name='not-found'),
    path('about-us/', views.get_about_us, name='about-us'),
    path('add-book/', views.get_add_book, name='add-book-page'),
    path('add-book/add/', views.add_book, name='add_book'),
    path('edit-book/<int:id>/', views.edit_book, name='edit-book'),
    path('delete/<int:id>/', views.delete, name='delete-book'),
]