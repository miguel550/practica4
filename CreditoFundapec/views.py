from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.db.models import Count, Sum
from django.urls import reverse_lazy
from rest_framework import viewsets
from .models import Estudiante, Credito, Transaccion
from .forms import EstudianteForm
from .serializers import EstudianteSerializer, TransaccionSerilizer

class ListaEstudiantes(ListView):
    model = Estudiante
    context_object_name = 'all_estudiantes'

    def get_queryset(self):
        qs = super(ListaEstudiantes, self).get_queryset()
        qs = qs.annotate(desembolsado=Sum('credito__transaccion__monto'),
                         num_pagos=Count('credito__transaccion'))
        return qs


class CrearEstudiante(FormView):
    form_class = EstudianteForm
    template_name = 'CreditoFundapec/estudiante_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        monto = form.cleaned_data.pop('monto')
        e = Estudiante(**form.cleaned_data)
        e.save()
        Credito(estudiante=e, monto=monto).save()
        return super(CrearEstudiante, self).form_valid(form)


class ListaTransacciones(ListView):
    model = Transaccion
    context_object_name = 'all_transacciones'

    def get_queryset(self):
        qs = super(ListaTransacciones, self).get_queryset()
        return qs


class TransaccionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows transacciones to be posted.
    """
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerilizer


class EstudianteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows estudiantes to be viewed or edited.
    """
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
