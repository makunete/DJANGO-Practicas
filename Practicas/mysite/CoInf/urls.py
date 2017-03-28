from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^compres/', views.CompresCreateView.as_view(success_url='/CoInf/fet'), name="compres" ),
    url(r'^incidencies/', views.IncidenciesCreateView.as_view(success_url="/CoInf/Infet"), name="incidencies" ),
    url(r'^fet/', views.CompresListView.as_view()),
    url(r'^Infet/', views.IncidenciesListView.as_view()),
    url(r'^Indesc/',views.IncidenciesDescListView.as_view()),
]