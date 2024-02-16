from django.shortcuts import render, HttpResponse, redirect

from .models import Teny

from random import randint

# Create your views here.

def szia_view(request):
    template = 'index.html'
    tenyek = list(Teny.objects.all())     # list parancs kicsit túlzás, de most egyszerűsítünk
    r = randint(0, len(tenyek)-1)
    context = {
        'esemeny_neve': tenyek[r].nev,
        }
    return render(request, template, context)

def valasz_view(request):
    template = 'valasz.html'
    if request.method == 'POST':
        kerdes = request.POST['kerdes']
        valasz = request.POST['valasz']
        print(f'A felhasználó a {kerdes} kérdésre ezt válaszolta: {valasz} ')
        teny = Teny.objects.filter(nev=kerdes).first()
        if teny == None:
            return HttpResponse('tudod kivel szórakozzál kisköcsög')
        
        if valasz == teny.ido:
            context = {'ertekeles':'jo'}
        
        else:
            context = {'ertekeles':'rossz'}
        return render(request, template, context)

    else:
        return redirect('kezdooldal')
