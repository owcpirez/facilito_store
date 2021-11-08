from django.shortcuts import render
from django.http import HttpResponse

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

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
    return render(request, 'users/login.html', {

    })