from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
		# login page
		#this version of Django does not work with this url 
		#url(r'^login/$', login, {'template_name' : 'users/login.html'}, name = 'login'),		
		# login page 
		url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
		# log out page 
		url(r'^logout/$',views.logout_view,name='logout'),
		# register page 
		url(r'^register/$',views.register,name='register'),
]
