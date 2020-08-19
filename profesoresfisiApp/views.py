from django.shortcuts import render
from .models import Profesor
from .models import Articulo
from django.db.models import Count

# Create your views here.
def profesores_list(request):
    profesores = Profesor.objects.all()
    profesores_t = Articulo.objects.all().values('profesor').annotate(total=Count('profesor')).order_by('profesor')
    articulos_a = Articulo.objects.all().values('anio','profesor').annotate(total=Count('anio')).order_by('profesor')
    articulos = Articulo.objects.all().order_by('anio')
    return render(request, 'profesoresfisiApp/profesores_list.html', {'profesores_t':profesores_t,'articulos':articulos,'profesores':profesores,'articulos_a':articulos_a})