from django.conf.urls import url

from api import views


urlpatterns = [
    url(r'^users/$', views.UserListCreateAPIView.as_view(), name='list_create_users'),
]
