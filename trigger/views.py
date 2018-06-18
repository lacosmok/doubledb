from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import ExampleModel


# Create your views here.
class CreateExampleModel(CreateView):
    model = ExampleModel
    template_name = 'create_event.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        c = super(CreateExampleModel, self).form_valid(form)
        return c


class ExampleModelList(ListView):
    model = ExampleModel
    template_name = 'event_list.html'

    def get_queryset(self):
        #print(len( self.model.objects.using('seconddb').all()))
        return self.model.objects.using('seconddb').all()


class FullExampleModelList(ListView):
    model = ExampleModel
    template_name = 'event_list.html'

    def get_queryset(self):
        #print(len(self.model.objects.all()))
        return self.model.objects.all()


class EditExampleModel(UpdateView):
    model = ExampleModel
    template_name = 'create_event.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        c = super(EditExampleModel, self).form_valid(form)
        form.instance.double_save()
        return c


class DeleteExampleModel(DeleteView):
    model = ExampleModel
    success_url = reverse_lazy('index')
    template_name = 'confirm_delete_event.html'
