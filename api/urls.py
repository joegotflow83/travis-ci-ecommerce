from django.conf.urls import url

from api import views


urlpatterns = [
    url(r'^users/$', views.UserListCreateAPIView.as_view(), name='l_c_users'),
    url(r'^user/(?P<pk>\d+)/$', views.UserRetrieveUpdateDestoryAPIView.as_view(), name='r_u_d_user'),
]
