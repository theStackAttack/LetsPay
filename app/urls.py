from django.conf.urls import url,include
from . import views as app_v


from django.contrib.auth import views
from app.forms import LoginForm


urlpatterns = [
    url(r'^$',app_v.index, name='home'),
    url(r'^login/$', views.login, {'template_name': 'app/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/app/'}, name='logout'),
    url(r'^register/$', app_v.register, name="register"),
    url(r'^success/', app_v.success, name="success"),
    url(r'^success1/', app_v.success1, name="success1"),
    url(r'^check/username/(?P<username>[-\w.]+)/$', app_v.check),
    url(r'^create/$', app_v.createPromo, name="createPromo"),
    url(r'^withdraw/$', app_v.withdrawPromo, name="withdrawPromo"),
    url(r'^sendOtp/$', app_v.sendOtp),
    url(r'^getToken/$', app_v.get_token),
    url(r'^checkBalance/$', app_v.checkBalance),
    url(r'^generateChecksum/$', app_v.generateChecksum),
    url(r'^makeTransaction/$', app_v.makeTransaction),
    url(r'^doTransfer/$', app_v.doTransfer),
]