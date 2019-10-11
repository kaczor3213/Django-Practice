from django.shortcuts import render, Http404
from django.views import View
import my_project.urls

class ListApps(View):
    def get(self, request):
        context = {
            'apps':  [url.pattern.__str__()[0:-1] for url in my_project.urls.urlpatterns if url.pattern.__str__()]
        }
        return render(request, "navigator/index.html", context)
    def post(self, request):
        raise Http404
