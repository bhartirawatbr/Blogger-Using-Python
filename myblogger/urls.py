from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
# from core.apiset import ApiSet
# from apiset import ApiSet
admin.autodiscover()

# apiv1 = ApiSet(
# 				urls=[
			
# 						url(r'^user/',include('myblog.urls')),
# 						url(r'^docs/', include('rest_framework_swagger.urls'))
# 					]
# 				)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblogger.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    # url(r'^api/v1/', include(apiv1)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^user/',include('myblog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
