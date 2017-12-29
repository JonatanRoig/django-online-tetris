from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
from .models import Sesion, Castigo
from .forms import SesionForm, CastigoForm
from django.views.decorators.csrf import csrf_exempt

from django.template.loader import render_to_string
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
import simplejson as json

import time
import datetime
from datetime import timedelta
from django.utils import timezone

from django.db.models import Q

from random import randint

@csrf_exempt
def index(request):
    # return HttpResponse('Hello from Python!')

    if (request.method=='POST') and request.is_ajax():
        
        # Datos que mandamos de vuelta al HTML
        response_data={}

        # Recojemos el NICKNAME introducido
        nickname=request.POST.get('nickname')
        
        # Creamos el objeto SESION
        new_sesion = Sesion(nombre=nickname)
        new_sesion.save()
        
        response_data['user_pk']= new_sesion.pk


        return HttpResponse(json.dumps(response_data),content_type="application/json")

    else:

        return render(request, 'tetris_main.html')

@csrf_exempt
def get_score(request):
    # return HttpResponse('Hello from Python!')

    if (request.method=='POST') and request.is_ajax():
        

        # Recojemos el SCORE introducido
        score_actual=request.POST.get('score_actual')

        # Recojemos el USER_PK introducido
        user_pk=request.POST.get('user_pk')
        
        user_pk = int(user_pk)

        # Obtenemos el objeto SESION correspondiente al usuario
        sesion = Sesion.objects.get(pk=user_pk)
        sesion.puntos = score_actual
        sesion.save()
        

        # Datos que mandamos de vuelta al HTML
        response_data={}

        # Barrera de tiempo que sirve como tope para decir a partir 
        # de que punto ya no se considera activa la sesion
        now = timezone.now()
        time_limit_barrier = now - datetime.timedelta(minutes=5)

        # Capturamos todos los objetos Sesion existentes en la base de datos
        all_sesions = Sesion.objects.filter(last_updated__range=(time_limit_barrier,now)).order_by('-puntos')


        # Renderizamos el marcador de puntuaciones en un string html
        response_data['html_scores']=render_to_string("marcador.html",{'all_sesions':all_sesions, 'user_pk': user_pk })

        response_data['user_velocidad'] = sesion.velocidad


        return HttpResponse(json.dumps(response_data),content_type="application/json")

    else:

        return HttpResponse(json.dumps({"nothing to see":"this isn't happening"}),content_type="application/json")



@csrf_exempt
def get_castigs(request):


    if (request.method=='POST') and request.is_ajax():

        # Recojemos el USER_PK introducido
        user_pk=request.POST.get('user_pk')

        user_pk = int(user_pk)

        # Obtenemos el objeto SESION correspondiente al usuario
        sesion = Sesion.objects.get(pk=user_pk)

        all_castigos = Castigo.objects.filter( Q(emisor=sesion) | Q(receptor=sesion) ).order_by('-created')

        # Datos que mandamos de vuelta al HTML
        response_data={}

        # Renderizamos el marcador de puntuaciones en un string html
        response_data['html_castigos']=render_to_string("castigos.html",{'all_castigos':all_castigos, 'user_pk': user_pk })

        response_data['numero_castigos'] = len(Castigo.objects.filter(receptor=sesion))

        return HttpResponse(json.dumps(response_data),content_type="application/json")

    else:

        return HttpResponse(json.dumps({"nothing to see":"this isn't happening"}),content_type="application/json")




@csrf_exempt
def new_castig(request):


    if (request.method=='POST') and request.is_ajax():

        # Recojemos el USER_PK introducido
        user_pk=request.POST.get('user_pk')

        user_pk = int(user_pk)

        # Obtenemos el objeto SESION correspondiente al usuario
        sesion = Sesion.objects.get(pk=user_pk)

        # Escollim receptor entre sesion actives en la BD
        
        # Capturamos todos los objetos Sesion existentes en la base de datos
         # Barrera de tiempo que sirve como tope para decir a partir 
        # de que punto ya no se considera activa la sesion
        now = timezone.now()
        time_limit_barrier = now - datetime.timedelta(minutes=5)

        # Capturamos todos los objetos Sesion existentes en la base de datos
        all_sesions = Sesion.objects.filter(last_updated__range=(time_limit_barrier,now)).order_by('-puntos').exclude(pk=sesion.pk)



        # Si existe algún otro usuario activo elegimos aleatoriamente a cual le enviamos el castigo
        if all_sesions:
            num_sesions = len(all_sesions)

            receptor_random = randint(0, num_sesions - 1)
            
            receptor_random = all_sesions[receptor_random]


            # Busquem un random de 0 a num_sesions i assignem all_sesions[random] a receptor
            
            new_castigo = Castigo(emisor=sesion, receptor=receptor_random)
            new_castigo.save()

            # Cambiamos las velocidades del usuario actual y del receptor
            sesion.reducir_velocidad()
            sesion.save()

            receptor_random.augmentar_velocidad()
            receptor_random.save()
        
        # Datos que mandamos de vuelta al HTML
        response_data={}

        
        return HttpResponse(json.dumps(response_data),content_type="application/json")

    else:

        return HttpResponse(json.dumps({"nothing to see":"this isn't happening"}),content_type="application/json")






class SesionListView(ListView):
    model = Sesion


class SesionCreateView(CreateView):
    model = Sesion
    form_class = SesionForm


class SesionDetailView(DetailView):
    model = Sesion


class SesionUpdateView(UpdateView):
    model = Sesion
    form_class = SesionForm


class CastigoListView(ListView):
    model = Castigo


class CastigoCreateView(CreateView):
    model = Castigo
    form_class = CastigoForm


class CastigoDetailView(DetailView):
    model = Castigo


class CastigoUpdateView(UpdateView):
    model = Castigo
    form_class = CastigoForm

