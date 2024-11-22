
from django.http import HttpResponse
from django.template import loader

def calculator_view(request):
    template = loader.get_template('cal.html')
    return HttpResponse(template.render())

# Create your views here.
