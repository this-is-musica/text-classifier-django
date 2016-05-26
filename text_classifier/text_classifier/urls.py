from django.conf.urls import include, url
from django.contrib import admin
from money_maker import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r"test/", views.test, name="test"),
    url(r'^admin/', include(admin.site.urls)),
]
