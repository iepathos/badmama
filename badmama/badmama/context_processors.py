from django.contrib.sites.models import Site

def default(request):
	"""
	provide current site object in default context

	allows access to site.domain and site.name
	"""
	return {
	    'site' : Site.objects.get_current(),
	}