from django.urls import path #import path func
from . import views #ref view func in current path

#URL Conf:
#define special var: this is what django looks for:
#array of URL pattern objects

# views.XX : XX = the name of the function in views
urlpatterns = [
    path('', views.pagina_principala, name='home'), #default endpoint / website (localhost in this case)
    path('info/', views.pagina_info, name='info'),
    path('search/', views.test_params, name='test_q'), #test - returns URL parameter
    path('postendpoint/', views.post_exp, name='post_ex'),
    path('submit_exp/', views.submit_exp, name='submit_ex'), #test - function that validates user input
    path('submit_django/', views.django_form, name='submit_dj_f') #test for user valdiaiton using form
]
