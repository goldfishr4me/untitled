from django.conf.urls import url
from .views import HomeView, AboutView, PeopleView
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    url(r'home', HomeView.as_view(), name='home'),
    url(r'About', AboutView.as_view(), name='about'),
    url(r'People', PeopleView.as_view(), name='people'),
    # url(r'^pages/',	include('django.contrib.flatpages.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
