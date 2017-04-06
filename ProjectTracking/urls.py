from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from ProjectTracking.views import IndexView, login_view, logout_view, add_view, change_view

urlpatterns = [
    url(r'^$', login_required(IndexView.as_view()), name='index'),
    # url(r'^login/$', LoginView.as_view(), name='index'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^requirement/add/', add_view, name='add'),
    url(r'^requirement/change/', change_view, name='change'),
]