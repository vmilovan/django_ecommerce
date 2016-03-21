from django.conf.urls import patterns, include, url

from django.contrib import admin
from payments import views
admin.autodiscover()

urlpatterns = patterns(
    '',
    # index
    url(r'^$', 'main.views.index', name='home'),

    # pages
    url(r'^pages/', include('django.contrib.flatpages.urls')),

    # contact
    url(r'^contact/', 'contact.views.contact', name='contact'),

    # payments
    url(r'^sign_in$', views.sign_in, name='sign_in'),
    url(r'^sign_out$', views.sign_out, name='sign_out'),
    url(r'^register$', views.register, name='register'),
    url(r'^edit$', views.edit, name='edit'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
