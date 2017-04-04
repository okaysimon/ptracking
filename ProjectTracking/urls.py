from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from ProjectTracking.views import IndexView, login_view, logout_view

urlpatterns = [
    url(r'^$', login_required(IndexView.as_view()), name='index'),
    # url(r'^login/$', LoginView.as_view(), name='index'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
]