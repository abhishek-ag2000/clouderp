from django import forms
from blog.models import Blog


class DateInput(forms.DateInput):
    input_type = 'date'

class Blogform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(Blogform, self).__init__(*args, **kwargs)
		self.fields['Category'].widget.attrs = {'class': 'form-control select2', 'placeholder':"Select Category",}
		self.fields['Date'].widget.attrs = {'class': 'form-control'}		
	
	Blog_title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
	class Meta:
		model = Blog
		fields = ['Date', 'Blog_title', 'Description', 'Blog_image', 'Category']
		widgets = {
            'Date': DateInput(),
        }


class BlogSearchForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))