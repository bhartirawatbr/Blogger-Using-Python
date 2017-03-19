from myblog import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^register/$', views.Register.as_view(), name='register'),
    # url(r'^category/$',views.CategoryView.as_view(),name='category'),
    url(r'^emailverify/$',views.EmailVerify.as_view(),name='emailverify'),
    url(r'^email_verify_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.EmailVerifyConfirm.as_view(),name='email_verify_confirm'),
    )