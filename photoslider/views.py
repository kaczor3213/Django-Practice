from django.shortcuts import render, Http404
from django.views import View
from os import listdir
from os.path import isfile, join

class SliderView(View):
    def get(self, request):
        #images = [f for f in listdir('./images') if isfile(join('./images', f))]
        return render(request, 'photoslider/slider.html', {})
    def post(self, request):
        pass
