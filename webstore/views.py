from django.http import HttpResponse
from django.shortcuts import render

def pagina_principala(request):
    # displays proj info desc.
    descriere = """
        Welcome to webstore:  
        Acest proiect reprezintă magazinul online al unui magazin de bijuterii. 
        Platforma le va permite utilizatorilor să își creeze un cont, să exploreze 
        colecțiile disponibile și să plaseze comenzi sau să inițieze retururi.
        """
    return HttpResponse(descriere) #returns simple plaintext http response

def pagina_info(request):
    #loads HTML template for info page
    return render(request, 'info.html') #RENDERS an HTML page

