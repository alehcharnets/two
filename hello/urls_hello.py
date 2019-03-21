from django.urls import re_path
from . import views
# from django.urls import reverse_lazy
# form django.contrib.auth.views import LogoutView
# from django.views.generic import ListView, DetailView


urlpatterns = [
    re_path(r'^$', views.ShowAll),
    re_path('world/', views.hello),
    re_path('name/', views.names),
    re_path('all/', views.ShowAll, name='video_all_url'),
    re_path(r'^get/(?P<video_id>\d+)/$', views.OneVideo, name='one_video_url'),
    re_path(r'^addlike/ajax/$', views.LikeaJax, name='ajax_url'),
    re_path(r'^adddislike/ajax/$', views.DisLikeaJax, name='dis_ajax_url'),
    re_path(r'^addcomment/(?P<video_id>\d+)/$', views.AddComment,
            name='addcomment_url'),
    re_path(r'^search/$', views.Search, name='search_url'),
    re_path(r'^registration/$', views.Registration, name='registration_url'),
    re_path(r'^login/$', views.Login, name='login_url'),
    re_path(r'^logout/$', views.Logout, name='logout_url')
]

# <pk> - праймер кей, вместо id
