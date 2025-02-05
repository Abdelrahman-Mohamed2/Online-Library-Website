from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.get_home_user, name='home-user'),
    path('<int:id>', views.get_book_details, name='book-details2'),
    path('borrow-book/<int:id>/', views.borrow_book, name='borrow'),
    path('remove-book/<int:id>/', views.remove_book, name='remove'),
    path('not-found/', views.get_not_found, name='not-found'),
    path('about-us/', views.get_about_us, name='about-us'),
    path('list-borrowed/', views.get_list_borrowed, name='list-borrowed'),
]