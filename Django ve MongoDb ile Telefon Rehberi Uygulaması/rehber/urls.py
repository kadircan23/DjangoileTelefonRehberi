from django.conf.urls import url, include

from rehber.views import home_wiev, index_wiev, detail_wiev, kisi_ekle_view, kisi_sorgula_view, search_tel_number,update_wiev,delete_wiev
from . import views

app_name='rehber'
urlpatterns = [
    url(r'^$',home_wiev),
    url(r'^index$', index_wiev),
    url(r'^(?P<id>\d+)/$', detail_wiev),
    url(r'^kisiekle$', kisi_ekle_view),
    url(r'^kisisorgula$', kisi_sorgula_view),
    url(r'^ajaxsearch/$', search_tel_number),
    url(r'^(?P<id>\d+)/update/$', update_wiev),
    url(r'^(?P<id>\d+)/delete/$', delete_wiev),

]