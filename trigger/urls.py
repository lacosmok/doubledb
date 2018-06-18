from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.ExampleModelList.as_view(), name='index'),
    path(r'full/', views.FullExampleModelList.as_view(), name='full-list'),
    path(r'create/examplemodel/', views.CreateExampleModel.as_view(), name='create-example-model'),
    path(r'edit/examplemodel/<int:pk>', views.EditExampleModel.as_view(), name='edit-example-model'),
    path(r'delete/examplemodel/<int:pk>', views.DeleteExampleModel.as_view(), name='delete-example-model'),

]