from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView



class TestPage(TemplateView):
    template_name = 'clouderp/test.html'  
     
class HomePage(TemplateView):
	template_name = "clouderp/index.html"


class BlogPage(TemplateView):
	template_name = "puput/blog.html"



	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return HttpResponseRedirect(reverse("test"))
		return super().get(request, *args, **kwargs)

