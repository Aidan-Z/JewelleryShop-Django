from django.urls import path #import path func
from . import views #ref view func in current path

#URL Conf:
#define special var: this is what django looks for:
#array of URL pattern objects
urlpatterns = [
    path('', views.pagina_principala, name='home'),
    path('info/', views.pagina_info, name='info'),
]
