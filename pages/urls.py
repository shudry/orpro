from django.conf.urls import url
from .views import *



urlpatterns = [
url(r'^goods/(?P<off_url>[A-Za-z0-9_-]+)/$', OfferAjaxUpdateView.as_view(), name='offer'),
url(r'^goods/(?P<off_url>[A-Za-z0-9_-]+)/images/$', OfferImagesAjaxUpdateView.as_view(), name='offer_images'),
url(r'^1g$', pars_cat),
url(r'^2g$', pars_goods),
url(r'^catalog/(?P<cat_url>[A-Za-z0-9_-]+)$', catalog, name='catalog'),
url(r'^otzyvy', review, name='review'),
url(r'^catalog', catalog, name='cat_redirect'),
url(r'^api-import$', api_import, name='api_import'),
url(r'^(?P<post_seourl>[A-Za-z0-9_-]+)$', singlepage),
url(r'^$', home, name='home'),
]
