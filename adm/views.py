from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Book



def get_home_admin(request):
    username = request.session.get('username')
    context = {
        'books' : Book.objects.all(),
        'username': username
    }
    return render(request, 'home-admin.html',context)

def get_about_us(request):
    username = request.session.get('username')
    context = {
        'username': username
        }
    return render(request, 'about-us-admin.html', context)

def get_book_details(request, id):
    book_id = Book.objects.get(id=id)
    username = request.session.get('username')
    context = {
        'book': book_id,
        'username': username
        }
    return render(request, 'book-Details-Admin.html', context)

def get_not_found(request):
    username = request.session.get('username')
    context = {
        'username': username
        }
    return render(request, 'not-found-admin.html', context)

def get_add_book(request):
    username = request.session.get('username')
    context = {
        'username': username
        }
    return render(request, 'add-book.html', context)

@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        category = request.POST['category']
        author = request.POST['author']
        description = request.POST['description']
        if title and category and author and description:
            new_book = Book(
                title=title,
                category=category,
                author=author,
                description=description,
                available=True
            )
            new_book.save()
            return redirect('/adm/home')
        else:
            return render(request, 'add-book.html', {'error': 'All fields are required'})
    return render(request, 'add-book.html')
    

def edit_book(request, id):
    try:
        book_instance = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return redirect('not-found')
    username = request.session.get('username')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        author = request.POST.get('author')
        description = request.POST.get('description')
        
        if title and category and author and description:
            book_instance.title = title
            book_instance.category = category
            book_instance.author = author
            book_instance.description = description
            book_instance.save()
            return redirect('book-details', id=book_instance.id)
    
    context = {
        'book': book_instance,
        'username': username
    }
    return render(request, 'edit-book.html', context)


def delete(request,id):
    username = request.session.get('username')
    book_delete = get_object_or_404(Book,id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/adm/home')
    context = {
        'book': book_delete,
        'username': username
        }
    return render(request, 'delete.html', context)