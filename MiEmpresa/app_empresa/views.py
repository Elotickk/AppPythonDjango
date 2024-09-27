from django.shortcuts import render
from .models import Cliente
from django.shortcuts import render, redirect
from .forms import ClienteForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render (request,'app_empresa/index.html')

def listado(request):
    clientes= Cliente.objects.all () 
    return render (request, 'app_empresa/listado.html',{'clientes':clientes})

def nuevo_cliente(request):
    if request.method == 'POST':
        formcliente = ClienteForm(request.POST, request.FILES)
        if formcliente.is_valid():
            formcliente.save()
            messages.success(request, 'Cliente creado exitosamente.')
            return redirect('index')
        else:
            messages.error(request, 'Atención: Verifique los Datos Ingresados')
    else:
        formcliente = ClienteForm()
    return render(request, 'app_empresa/nuevo_cliente.html', {'formcliente': formcliente})