from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render

#for TEST/LEARNING form class:
from .forms import PersonForm


# endpoints need to be created in urls.py for all of these 



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



#OLD VERSION -> PRE form class | new below:
# the html from 'submit_expl.html' is rendered by this view
# views needs to validate input when this page accesses, so passes to a form (updated)
# def post_exp(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         age = request.POST.get('age')
#         return HttpResponse(f"{name}, {age}")
#     else:
#         return HttpResponseNotAllowed('POST')


def post_exp(request):
    if request.method == "POST":
        form = PersonForm(request.POST) #feed the post info right into class upon initialization 

        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']

            return HttpResponse(f"POsted: ->> {name}, {age}")
        else:
            return HttpResponseNotAllowed('POST')


def submit_exp(request):
    return render(request, 'webstore/submit_expl.html')


def django_form(request): #pass empty form object as context to rendering
    form = PersonForm()
    return render(request, 'webstore/submit_django_form.html',{'form': form})