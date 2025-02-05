from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import User

def get_login_page(request):
    return render(request, 'login.html')

def get_signup_page(request):
    return render(request, 'sign-up.html')

@csrf_protect
def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        is_admin = request.POST['radio'] == 'Admin'

        if password != confirm_password:
            return render(request, 'sign-up.html', {
                'error': "Your confirmation password must match.",
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'sign-up.html', {
                'error': "The username is not available.",
            })

        if User.objects.filter(email=email).exists():
            return render(request, 'sign-up.html', {
                'error': "This email address is already used.",
            })

        user = User(username=username, email=email, password=password, isadmin=is_admin)
        user.save()
        return redirect('login')

    return render(request, 'sign-up.html')

@csrf_protect
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if user.password == password:
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                request.session['is_admin'] = user.isadmin
                if(user.isadmin):
                    return redirect('/adm/home')  
                else:
                    return redirect('/user/home')  
            else:
                return render(request, 'login.html', {
                    'error': "Incorrect username or password.",
                })
        else:
            return render(request, 'login.html', {
                    'error': "Incorrect username or password.",
                })
    return render(request, 'login.html')