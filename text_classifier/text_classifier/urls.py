from django.conf.urls import include, url
from django.contrib import admin
from money_maker import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'text_classifier.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', views.index),
    url(r'^admin/', include(admin.site.urls)),
]
