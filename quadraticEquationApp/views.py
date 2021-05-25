from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.template import loader
from django.shortcuts import get_list_or_404
from django.urls import reverse
from .models import Equation


# Create your views here.

def equation_input(request):
    equation = Equation()
    template = loader.get_template('quadraticEquationApp/form.html')
    context = {'equation': equation}
    return HttpResponse(template.render(context, request))


def eq_list(request):
    list = Equation.objects.order_by('id')
    template = loader.get_template('quadraticEquationApp/eqList.html')
    context = {'eq_list': list}

    return HttpResponse(template.render(context, request))


def save_and_list(request):
    if request.method == "POST":
        a = request.POST['a']
        b = request.POST['b']
        c = request.POST['c']
        if a != '' and b != '' and c != '':
            eq = Equation(a=a, b=b, c=c)
            eq.save()
        else:
            return render(request, 'quadraticEquationApp/form.html', {'error_message': "Fill in all the fields"})

    return HttpResponseRedirect(reverse('quadraticEquationApp:eqList'))


def calculate(request, equation_id):
    e = Equation.objects.get(pk=equation_id)
    D = e.b ** 2 - 4 * e.a * e.c

    if D >= 0:
        e.x1 = (-e.b + D ** 0.5) / (2 * e.a)
        e.x2 = (-e.b - D ** 0.5) / (2 * e.a)
        e.save()

    return HttpResponseRedirect(reverse('quadraticEquationApp:eqList'))


class EqList(generic.ListView):
    template_name = 'quadraticEquationApp/eqList.html'
    context_object_name = 'equations'

    def get_queryset(self):
        return Equation.objects.order_by('id')[:]
