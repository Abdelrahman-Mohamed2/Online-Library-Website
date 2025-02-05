from django.shortcuts import render,redirect,get_object_or_404
from adm.models import Book
from Authentication.models import User

def get_home_user(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')
    context = {
        'books' : Book.objects.all(),
        'username': username
    }
    return render(request, 'home-user.html',context)

def get_about_us(request):
    username = request.session.get('username')
    context = {
        'username': username
        }
    return render(request, 'about-us-user.html', context)

def get_book_details(request,id):
    book_id = Book.objects.get(id=id)
    username = request.session.get('username')
    context = {
        'book': book_id,
        'username': username
        }
    return render(request, 'book-details-user.html', context)

def get_not_found(request):
    username = request.session.get('username')
    context = {
        'username': username
        }
    return render(request, 'not-found-user.html', context)

def get_list_borrowed(request):
    userid = request.session.get('user_id')
    user = get_object_or_404(User, id=userid)
    user_books = user.borrowed_books.all
    username = request.session.get('username')
    context = {
        'books': user_books,
        'username': username
        }
    return render(request, 'list-borrowed.html', context)

def borrow_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        if book.available:
            book.available = False
            book.save()
            userid = request.session.get('user_id')
            user = get_object_or_404(User, id=userid)
            user.borrowed_books.add(book)
        return redirect('/user/home')
    username = request.session.get('username')
    context = {
        'book': book,
        'username': username
        }
    return redirect('book-details', context)

def remove_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        if not book.available:
            book.available = True
            book.save()
            userid = request.session.get('user_id')
            user = get_object_or_404(User, id=userid)
            user.borrowed_books.remove(book)
        return redirect('list-borrowed')
    username = request.session.get('username')
    context = {
        'book': book,
        'username': username
        }
    return redirect('book-details', context)