from django.shortcuts import render, Http404
from django.views import View
from .models import *

class SliderView(View):
    def get(self, request):
        context = {
            'indices' : [p.pk-Photo.objects.first().pk for p in Photo.objects.all()],
            'images' : Photo.objects.all(),
        }
        return render(request, 'photoslider/slider.html', context)
    def post(self, request):
        pass
