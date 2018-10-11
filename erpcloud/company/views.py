from django.shortcuts import render
from django.views.generic import (ListView,DetailView,
								  CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from company.models import company
from company.forms import companyform,daterangeform
from django.shortcuts import redirect
from todogst.models import Todo
from accounting_double_entry.models import selectdatefield

# Create your views here.


class FormListView(FormMixin, ListView):
    def get(self, request, *args, **kwargs):
        # From ProcessFormMixin
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

        # From BaseListView
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})

        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class companyListView(LoginRequiredMixin,FormListView):
	model = company
	form_class  = daterangeform
	paginate_by = 10

	def get_queryset(self):
		return company.objects.filter(User=self.request.user)

	def get_context_data(self, **kwargs):
		context = super(companyListView, self).get_context_data(**kwargs)
		context['selectdate'] = selectdatefield.objects.filter(User=self.request.user).latest('Start_Date')
		return context

class companyDetailView(LoginRequiredMixin,DetailView):
	context_object_name = 'company_details'
	model = company
	template_name = 'company/Dashboard.html'

	def get_context_data(self, **kwargs):
		context = super(companyDetailView, self).get_context_data(**kwargs)
		context['todo_list'] = Todo.objects.filter(User=self.request.user).order_by('-id')
		return context


class companyCreateView(LoginRequiredMixin,CreateView):
	form_class  = companyform
	template_name = "company/company_form.html"

	def form_valid(self, form):
		form.instance.User = self.request.user
		return super(companyCreateView, self).form_valid(form)


class companyUpdateView(LoginRequiredMixin,UpdateView):
	model = company
	form_class  = companyform
	template_name = "company/company_form.html"

class companyDeleteView(LoginRequiredMixin,DeleteView):
	model = company
	success_url = reverse_lazy("company:list")

class selectdaterangecreate(LoginRequiredMixin,CreateView):
	form_class  = daterangeform
	template_name = "company/selectdate.html"

class selectdaterange(LoginRequiredMixin,UpdateView):
	model = selectdatefield
	form_class  = daterangeform
	template_name = "company/selectdate.html"

	def form_valid(self, form):
		form.instance.User = self.request.user
		return super(selectdaterange, self).form_valid(form)



# class Todolist(LoginRequiredMixin,ListView):
# 	model = Todo
# 	paginate_by = 10

# 	def get_queryset(self):
# 		return Todo.objects.filter(User=self.request.user)

# 	def post(self, request, *args, **kwargs):
# 		return TodoUpdate.as_view()(request)

# class TodoCreate(LoginRequiredMixin,CreateView):
# 	form_class = Todoform
# 	template_name = 'company/todo_form.html'

# 	def form_valid(self, form):
# 		form.instance.User = self.request.user
# 		return super(TodoCreate, self).form_valid(form)


# class TodoUpdate(LoginRequiredMixin,UpdateView):
# 	model = Todo
# 	form_class = Todoform
# 	template_name = 'company/todo_form.html'


# class TodoDelete(LoginRequiredMixin,UpdateView):
# 	model = Todo
# 	success_url = reverse_lazy("company:Todolist")

# 	def get(self, *args, **kwargs):
# 		return self.delete(*args, **kwargs)

# class Tododelete(LoginRequiredMixin,DeleteView):
# 	model = Todo
# 	success_url = reverse_lazy("company:Dashboard")
# 	template_name = 'company/todo_confirm_delete.html'

# 	def get(self, *args, **kwargs):
# 		return self.delete(*args, **kwargs)


# def deleteCompleted(request):
# 	Todo.objects.filter(complete__exact=True).delete()

# 	return redirect('company:Dashboard')
