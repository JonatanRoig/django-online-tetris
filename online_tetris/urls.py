from django.conf.urls import url, include

from rest_framework import routers
from . import api
from . import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'sesion', api.SesionViewSet)
router.register(r'castigo', api.CastigoViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),

    url(r'^admin/', include(admin.site.urls) ),

	url(r'^$', views.index, name='index'),
	url(r'^get_score/$', views.get_score, name='get_score'),
	url(r'^get_castigs/$', views.get_castigs, name='get_castigs'),
    url(r'^new_castig/$', views.new_castig, name='new_castig'),
)


urlpatterns += (
    # urls for Sesion
    url(r'^online_tetris/sesion/$', views.SesionListView.as_view(), name='online_tetris_sesion_list'),
    url(r'^online_tetris/sesion/create/$', views.SesionCreateView.as_view(), name='online_tetris_sesion_create'),
    url(r'^online_tetris/sesion/detail/(?P<slug>\S+)/$', views.SesionDetailView.as_view(), name='online_tetris_sesion_detail'),
    url(r'^online_tetris/sesion/update/(?P<slug>\S+)/$', views.SesionUpdateView.as_view(), name='online_tetris_sesion_update'),
)

urlpatterns += (
    # urls for Castigo
    url(r'^online_tetris/castigo/$', views.CastigoListView.as_view(), name='online_tetris_castigo_list'),
    url(r'^online_tetris/castigo/create/$', views.CastigoCreateView.as_view(), name='online_tetris_castigo_create'),
    url(r'^online_tetris/castigo/detail/(?P<slug>\S+)/$', views.CastigoDetailView.as_view(), name='online_tetris_castigo_detail'),
    url(r'^online_tetris/castigo/update/(?P<slug>\S+)/$', views.CastigoUpdateView.as_view(), name='online_tetris_castigo_update'),
)

