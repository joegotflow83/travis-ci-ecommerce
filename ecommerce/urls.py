from django.conf.urls import url


from ecommerce import views


urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
]
