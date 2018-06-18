from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import Event


# Create your views here.
class CreateEvent(CreateView):
    model = Event
    template_name = 'create_event.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        c = super(CreateEvent, self).form_valid(form)
        return c


class EventList(ListView):
    model = Event
    template_name = 'event_list.html'

    def get_queryset(self):
        return self.model.objects.using('seconddb').all()


class FullEventList(ListView):
    model = Event
    template_name = 'event_list.html'

    def get_queryset(self):
        return self.model.objects.all()


class EditEvent(UpdateView):
    model = Event
    template_name = 'create_event.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        c = super(EditEvent, self).form_valid(form)
        form.instance.double_save()
        return c
