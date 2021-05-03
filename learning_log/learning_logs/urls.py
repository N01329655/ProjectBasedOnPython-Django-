from django.conf.urls import url
from . import views 
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^topics/$', views.topics, name = 'topics'),
	## page with the description of certain topic
	url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic')

]
