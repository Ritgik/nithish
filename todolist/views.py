
from django.http import HttpResponse
from django.template import loader

def todolist_view(request):
    template = loader.get_template('ind.html')
    return HttpResponse(template.render())
# Create your views here.