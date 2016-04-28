from django.conf.urls import include, url 
#from shortenersite.views import Shorten_url, Redirect_original, Index
import shortenersite.views
 
urlpatterns = [
    
    #url(r'^makeshort/(?P<pk>\d+)', Shorten_url.as_view(), name='shortenurl'),
    url(r'^makeshort/', shortenersite.views.shorten_url, name='shortenurl'),
    # this will create a URL's short id and return the short URL
    
    #url(r'^(?P&lt;short_id&gt;\w{6})', shortenersite.views.redirect_original, name='redirectoriginal'),
    #url(r'^(?P<short_id>\w{6})', Redirect_original.as_view(), name='redirectoriginal'),
    url(r'^(?P<short_id>\w{6})', shortenersite.views.redirect_original, name='redirectoriginal'),
    # when short URL is requested it redirects to original URL
    
    #url(r'^', Index.as_view(), name='index'),
    url(r'^', shortenersite.views.index, name='index'),
    # for our home/index page
    ]
