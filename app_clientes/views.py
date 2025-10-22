from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm


# LISTA
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'app_clientes/lista_clientes.html', {'clientes': clientes})

# CREATE
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'app_clientes/crear_cliente.html', {'form': form})

# UPDATE
def editar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'app_clientes/editar_cliente.html', {'form': form})

# DELETE
def eliminar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'app_clientes/eliminar_cliente.html', {'cliente': cliente})

# READ DETAIL
def ver_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    return render(request, 'app_clientes/ver_cliente.html', {'cliente': cliente})
