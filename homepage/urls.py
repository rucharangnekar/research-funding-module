"""homepage URL Configuration
"""
from django.conf.urls import url
from . import views

app_name='homepage'

urlpatterns = [
	url(r'^$', views.detail, name='detail'),
	url(r'^studentdashboard/$', views.index, name='index'),
	url(r'^studentform/$', views.retrievestud, name='retrievestud'),
	url(r'^teacher_dashboard/$', views.index1, name='index1'),
	url(r'^register/$', views.userformview.as_view(), name='register'),
	url(r'^login/$',views.login_user,name='login'),
	url(r'^logout/$',views.logout_user,name='logout'),
	url(r'^Student_Request/$',views.student_request, name='student_request'),
	url(r'^Teacher_home/$',views.notify,name='notify'),
	url(r'^accept/(?P<sid1>[0-9]+)/$',views.accept,name='accept'),
	url(r'^reject/(?P<sid>[0-9]+)/$',views.reject,name='reject'),
	url(r'^check/$',views.check,name='check'),
	url(r'^base/$',views.base,name='base'),
	url(r'^application/$',views.application,name='application'),
	url(r'^applicants/$',views.alll,name='alll'),
	url(r'^rejectform/(?P<sid2>[0-9]+)/$',views.rejectform,name='rejectform'),	

]




