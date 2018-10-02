from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

# Create your views here.
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^web/$', views.output, name='output'),
    
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
