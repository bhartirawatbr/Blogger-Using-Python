from myblog import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^email_verify/$', views.EmailVerify.as_view(), name='email_verify'),
    url(r'^category/$',views.CategoryView.as_view(),name='category'),
    )