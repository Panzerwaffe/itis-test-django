from django.http import HttpResponseRedirect
from ITIS_dj.settings import LOGIN_URL

except_urls = ["/accounts"]


class LoginRequiredMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		if not any([except_url in request.path_info for except_url in except_urls]):
			if not request.user.is_authenticated:
				return HttpResponseRedirect(LOGIN_URL)
		return self.get_response(request)
