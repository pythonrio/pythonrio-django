from django.conf.urls import include, url
from django.contrib import admin

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^', include('core.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^markdownx/', include('markdownx.urls')),
]
