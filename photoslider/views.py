from django.shortcuts import render, Http404
from django.views import View
from os import listdir
import os
from os.path import isfile, join

class SliderView(View):
    def get(self, request):
        images = [f for f in listdir('photoslider/static/images/') if isfile(join('photoslider/static/images/', f))]
        context = {
            'images' : images,
        }
        return render(request, 'photoslider/slider.html', context)
    def post(self, request):
        pass
