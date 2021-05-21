from django.views.generic import TemplateView
from django.http import HttpResponse

class HomePageView(TemplateView):
    template_name = "home.html"
