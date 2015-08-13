from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.http import HttpResponse, HttpResponseRedirect
from my_proj.actions import f
from django.template import RequestContext
from django.http import JsonResponse

class Pages(TemplateView):
    template_name = 'main/base.html'

    def get(self, request):
        context = RequestContext(request)

        if request.is_ajax():
            return JsonResponse({'Houses': f()})
        return render(request, self.template_name, context)