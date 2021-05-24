from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "home.html"
    
    def showitens(self, request):
        my_context = {
            "list_images": [1, 2, 3, 4, 5],
        }
        return render(request, "home.html", my_context)