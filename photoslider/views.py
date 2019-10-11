from django.shortcuts import render, Http404
from django.views import View
from django.core import serializers
from .models import *
from .forms import ClientForm


# def view(request, …):
    
#     …
#     render_template_to_response("my_template.html", {"my_data": js_data, …})
    

class SliderView(View):
    def get(self, request):
        form = ClientForm()
        context = {
            'form' : form,
            'photos' : serializers.serialize("json", Photo.objects.all()),
        }
        return render(request, 'photoslider/slider.html', context)
    def post(self, request):
        form = ClientForm(request.POST)
