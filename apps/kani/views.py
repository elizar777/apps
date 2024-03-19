from django.shortcuts import render
from apps.kani.models import InfoUser, Secondary

# Create your views here.
def index(request):
    
    infouser = InfoUser.objects.latest("id")
    secondary = Secondary.objects.latest("id")
    return render(request, "index.html", locals())
    
    

