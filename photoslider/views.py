from django.shortcuts import render, Http404
from django.views import View
from django.core import serializers
from .models import *

class SliderView(View):
    def get(self, request):        
        context = {
            'photos' : serializers.serialize("json", Photo.objects.all()),
        }
        return render(request, 'photoslider/slider.html', context)
    def post(self, request):
        raise Http404