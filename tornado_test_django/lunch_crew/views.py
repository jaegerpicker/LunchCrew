from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
# Create your views here.
class DjangoView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('django')