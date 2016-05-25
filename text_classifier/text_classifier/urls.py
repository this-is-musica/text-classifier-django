from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from money_maker import views


router = routers.DefaultRouter()



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^home/$', views.HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
