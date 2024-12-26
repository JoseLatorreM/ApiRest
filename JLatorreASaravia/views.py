from django.contrib.auth import authenticate
from rest_framework.views import APIView
from django.shortcuts import render

from django.shortcuts import render, redirect
from JLatorreASaravia.models import Compra
from django.shortcuts import render, get_object_or_404
# Create your views here.

def VistaCompras(request):
    SacarDatos = Compra.objects.all()
    return render(request, "ListadoVenta.html", {'SacarDatos':SacarDatos})

def Autor(request):
    return render (request, "Autor.html")

def Formulario(request):
    return render (request, "FormularioVenta.html")

def Login(request):
    return render (request, "Login.html")

def Menu(request):
    return render (request, "Menu.html")

def guardar_datos(request):
        rut = request.POST['Rut']
        producto = request.POST['Producto']
        cantidad = request.POST['Cantidad']
        iva = request.POST['Iva']
        valorventa = request.POST['Valor_Venta']
        total = request.POST['Total']
        SacarDatos = Compra(
            Rut=rut,
            Producto=producto,
            Cantidad=cantidad,
            Iva=iva,
            Valor_Venta=valorventa,
            Total=total
        )
        SacarDatos.save()
        return redirect("/")

def buscar_por_pk(request):
    if request.method == 'POST':
        rut = request.POST.get('pk', None)
        if rut is not None:
            objeto = get_object_or_404(Compra, Rut=rut)
            return render(request, 'ModificarDato.html', {'objeto': objeto, 'rut_buscado': rut})
    return render(request, 'error.html') 

def ModificarDato(request, rut):
    if request.method == 'POST':
        rut = request.POST.get('Rut')
        producto = request.POST.get('Producto')
        cantidad = request.POST.get('Cantidad')
        iva  = request.POST.get('Iva')
        valor_venta = request.POST.get('Valor_Venta')
        total = request.POST.get('Total')
    # Obtener el objeto existente
        objeto = get_object_or_404(Compra, Rut=rut)
    # Actualizar los campos
        objeto.Producto = producto
        objeto.Cantidad = cantidad
        objeto.Iva = iva
        objeto.Valor_Venta = valor_venta
        objeto.Total = total
        objeto.save()
        return redirect(VistaCompras)
    return render(request, 'error.html')

def borrar(request,id):
    SacarDatos = Compra.objects.get(id=id)
    SacarDatos.delete()
    return redirect(VistaCompras)    

from django.shortcuts import redirect  # Añade la importación de redirect

class LoginView(APIView):
    def get(self, request):
        return render(request, 'Login.html')  # Renderizar el formulario de login

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Validar el nombre de usuario y la contraseña
        user = authenticate(username=username, password=password)

        if user is not None:
            # Si el usuario existe y las credenciales son válidas
            # Realizar la lógica adicional aquí si es necesario, por ejemplo, iniciar sesión
            return redirect('Listado')  # Redirigir a la página Listado_Compras después del login exitoso
        else:
            # Si las credenciales son inválidas, renderizar nuevamente el formulario con un mensaje de error
            return render(request, 'Login.html', {'error': 'Credenciales inválidas'})
