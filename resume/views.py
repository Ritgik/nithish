
from django.http import HttpResponse
from django.template import loader

def resume_view(request):
    template = loader.get_template('temp.html')
    return HttpResponse(template.render())
# Create your views here.
