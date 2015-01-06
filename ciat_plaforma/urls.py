from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from settings import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ciat_plaforma.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name="indexgeneral.html")),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    #(r'^accounts/logout/$', 'notas.views.logout_page'),
    #url(r'^password_change/$',
    #                        'django.contrib.auth.views.password_change',
    #                        {'template_name': 'registration/password_change_form.html',
    #                        'post_change_redirect': '/foros/perfil/'},
    #                        name='password-change'),

    url(r'^comunicacion/', include('comunicacion.notas.urls')),
    url(r'^foros/', include('comunicacion.foros.urls')),
    url(r'^agendas/', include('comunicacion.agendas.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^tagging_autocomplete/', include('tagging_autocomplete.urls')),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

if DEBUG:
    urlpatterns += patterns('',
                (r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                )
