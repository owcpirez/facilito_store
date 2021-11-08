from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import authenticate

def index(request):
    return render(request, 'index.html', {
        'message': 'Listado de Productos',
        'tittle': 'Productos',
        'products': [
            {'tittle': 'Playera', 'price': 5, 'stock': True},
            {'tittle': 'Guarda Sol', 'price': 15, 'stock': True},
            {'tittle': 'Nevera', 'price': 25, 'stock': False}
        ]
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password) #None
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no validos')

    return render(request, 'users/login.html', {

    })