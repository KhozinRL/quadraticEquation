from . import views
from django.urls import path

app_name = 'quadraticEquationApp'
urlpatterns = [
    path('', views.equation_input, name='equation_input'),
    path('<int:equation_id>/', views.calculate, name='calculate'),
    path('all/', views.eq_list, name='eqList'),
    path('save/', views.save_and_list, name='save')
]
