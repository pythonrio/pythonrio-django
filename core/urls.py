
from django.conf.urls import url

import core.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', core.views.index, name='index'),
    url(r'^db', core.views.db, name='db'),
]
