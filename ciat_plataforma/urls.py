from django.conf.urls import *
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from settings import *
from analisis.analisis.views import BusquedaPaisView



from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns


urlpatterns = i18n_patterns('',
    # Examples:
    # url(r'^$', 'ciat_plaforma.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name="indexgeneral.html")),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'comunicacion.notas.views.logout_page'),
    url(r'^password_change/$',
                            'django.contrib.auth.views.password_change',
                            {'template_name': 'registration/password_change_form.html',
                            'post_change_redirect': '/foros/perfil/'},
                            name='password-change'),
    #urls para comunicacion
    url(r'^comunicacion/', include('comunicacion.notas.urls')),
    url(r'^foros/', include('comunicacion.foros.urls')),
    url(r'^agendas/', include('comunicacion.agendas.urls')),
    url(r'^contrapartes/', include('comunicacion.contrapartes.urls')),

    #urls para analisis organizacional
    url(r'^analisis/', include('analisis.analisis.urls')),
    url(r'^admin/pais/$', BusquedaPaisView.as_view()),

    #urls para monitoreo
    url(r'^monitoreo/', include('monitoreo.monitoreo.urls')),

    #urls para apps de terceros
    url(r'^admin/', include(admin.site.urls)),
    url(r'^selectable/', include('selectable.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^tagging_autocomplete/', include('tagging_autocomplete.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^rosetta/', include('rosetta.urls')),

)

urlpatterns += staticfiles_urlpatterns()

if DEBUG:
    urlpatterns += patterns('',
                (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                )
