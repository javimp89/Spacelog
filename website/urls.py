from django.conf.urls.defaults import *
from django.conf import settings
from transcripts.views import PageView, RangeView

urlpatterns = patterns('',
    # Example:
    # (r'^website/', include('website.foo.urls')),
    
    (r'^$', 'homepage.views.homepage'),
    url(r'^page/(?:(?P<timestamp>-?[0-9]+)/)?$', PageView.as_view(), name="view_page"),
    url(r'^(?P<start>-?[0-9]+)/$', RangeView.as_view(), name="view_range"),
)

if settings.DEBUG: # pragma: no cover
    urlpatterns += patterns('',
        (r'^' + settings.P_STATIC_URL[1:] + '(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.P_STATIC_ROOT
        }),
        # (r'^' + settings.MEDIA_URL[1:] + '(?P<path>.*)$', 'django.views.static.serve', {
        #     'document_root': settings.MEDIA_ROOT
        # }),
    )

