from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from company.models import company

# Create your views here.
class companyListView(LoginRequiredMixin,ListView):
	model = company
	paginate_by = 10

	def get_queryset(self):
		return company.objects.filter(User=self.request.user)

class SelectDateRange(ListView):
    template_name = "selectdaterange/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SelectDateRange, self).get_context_data(*args, **kwargs)
        query1 = self.request.GET.get('sd')
        query2 = self.request.GET.get('ed')
        context['query1'] = query1
        context['query2'] = query2
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query1 = method_dict.get('sd', None) # method_dict['q']
        query2 = method_dict.get('ed', None)
        if query1,query2 is not None:
            return company.objects.daterange(query1,query2)
        
        '''
        __icontains = field contains this
        __iexact = fields is exactly this
        '''