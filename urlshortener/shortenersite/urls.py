from django.conf.urls import include, url 
import shortenersite.views
 
urlpatterns = [
    
    url(r'^makeshort/', shortenersite.views.shorten_url, name='shortenurl'),
    # this will create a URL's short id and return the short URL
    
    #url(r'^(?P&lt;short_id&gt;\w{6})', shortenersite.views.redirect_original, name='redirectoriginal'),
    url(r'^(?P<short_id>\w{6})', shortenersite.views.redirect_original, name='redirectoriginal'),
    # when short URL is requested it redirects to original URL
    
    url(r'^', shortenersite.views.index, name='index'),
    # for our home/index page
    ]
