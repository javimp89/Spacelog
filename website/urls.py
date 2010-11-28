from django.conf.urls.defaults import *
from django.conf import settings
from transcripts.views import PageView, PhasesView, RangeView, ErrorView, OriginalView
from homepage.views import HomepageView
from search.views import SearchView

tspatt = r'-?\d{2}:\d{2}:\d{2}:\d{2}'

urlpatterns = patterns('',
    # Example:
    # (r'^website/', include('website.foo.urls')),
    
    url(r'^$', HomepageView.as_view(), name="homepage"),
    url(r'^page/$', PageView.as_view(), name="view_page"),
    url(r'^page/(?P<start>' + tspatt + ')/$', PageView.as_view(), name="view_page"),
    url(r'^(?P<start>' + tspatt + ')/$', RangeView.as_view(), name="view_range"),
    url(r'^(?P<start>' + tspatt + ')/(?P<end>' + tspatt + ')/$', RangeView.as_view(), name="view_range"),
    url(r'^phases/$', PhasesView.as_view(), name="phases"),
    url(r'^search/$', SearchView.as_view(), name="search"),
    url(r'^people/$', 'people.views.people', name="people"),
    url(r'^people/(?P<role>[-_\w]+)/$', 'people.views.people', name="people"),
    url(r'^glossary/$', 'glossary.views.glossary', name="glossary"),   
    url(r'^original/(?P<page>\d+)/$', OriginalView.as_view(), name="original"),   
)

if settings.DEBUG: # pragma: no cover
    urlpatterns += patterns('',
        (r'^' + settings.P_STATIC_URL[1:] + 'missions/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MISSIONS_STATIC_ROOT
        }),
        (r'^' + settings.P_STATIC_URL[1:] + '(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.P_STATIC_ROOT
        }),
        # (r'^' + settings.MEDIA_URL[1:] + '(?P<path>.*)$', 'django.views.static.serve', {
        #     'document_root': settings.MEDIA_ROOT
        # }),
        (r'^404/$', ErrorView.as_view()),
        (r'^500/$', ErrorView.as_view(error_code=500)),
    )

handler404 = ErrorView.as_view()
handler500 = ErrorView.as_view(error_code=500)

