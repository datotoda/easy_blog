from django.http import HttpResponse

# Create your views here.
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'
