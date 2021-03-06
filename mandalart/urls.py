from django.urls import path
from . import views

urlpatterns = [
    path('new', views.new, name="new"),
    path('create', views.create, name="create"),
    path('view/<int:mandal_id>', views.view, name="view"),
]