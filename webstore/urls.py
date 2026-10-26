from django.urls import path #import path func
from . import views #ref view func in current path

#URL Conf:
#define special var: this is what django looks for:
#array of URL pattern objects
urlpatterns = [
    path('', views.pagina_principala, name='home'), #default endpoint / website (localhost in this case)
    path('info/', views.pagina_info, name='info'),
    path('search/', views.test_params, name='test_q'), #test - returns URL parameter
    path('postendpoint/', views.post_exp, name='post_ex'),
    path('submit_exp/', views.submit_exp, name='submit_ex')
]
