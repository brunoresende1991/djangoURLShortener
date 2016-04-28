#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404, redirect
import random, string, json
from shortenersite.models import Urls
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.context_processors import csrf
#from django.core.urlresolvers import reverse
#from django.views.generic.edit import CreateView
#from django.views.generic import DetailView
#from django.views.generic.base import RedirectView
#from .models import Link
 
def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('shortenersite/index.html', c)
 
#class Index(CreateView):
#    model = Link
#    fields = ["url"]

#    def form_valid (self, form):
#        prev = Link.objects.filter(url=form.instance.url)
#        if prev:
#            return redirect ("shorten_url", pk=prev[0].pk)
#        return super(Index, self).form_valid(form)

def redirect_original(request, short_id):
    url = get_object_or_404(Urls, pk=short_id) # get object, if not        found return 404 error
    url.count += 1
    url.save()
    return HttpResponseRedirect(url.httpurl)

#class Redirect_original(RedirectView):
#     permanent = False
     
#     def get_redirect_url(self, *args, **kwargs):
#         return Link.expandir(kwargs["short_id"])
 
def shorten_url(request):
    url = request.POST.get("url", '')
    if not (url == ''):
        short_id = get_short_code()
        b = Urls(httpurl=url, short_id=short_id)
        b.save()
 
        response_data = {}
        response_data['url'] = settings.SITE_URL + "/" + short_id
        return HttpResponse(json.dumps(response_data),  content_type="application/json")
    return HttpResponse(json.dumps({"error": "error occurs"}), content_type="application/json")
 
#class Shorten_url(DetailView):
#     model = Link

def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    # if the randomly generated short_id is used then generate next
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        try:
            temp = Urls.objects.get(pk=short_id)
        except:
            return short_id
