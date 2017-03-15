from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^compres/', views.CompresCreateView.as_view(success_url="fet"), name="compres" ),
]