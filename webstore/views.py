from django.http import HttpResponse, HttpResponseNotAllowed
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
    return render(request, 'webstore/info.html') #RENDERS an HTML page






# testing / learn funcs
def test_params(request):
    return HttpResponse(f"query in URL: {request.GET.get('q')}")

def post_exp(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        return HttpResponse(f"{name}, {age}")
    else:
        return HttpResponseNotAllowed('POST')



def submit_exp(request):
    return render(request, 'webstore/submit_expl.html')

