from django import template

register = template.Library()

@register.filter(name= 'running_total')
def running_total(journal_list):
	return sum(d.Debit for d in journal_list)




@register.filter(name= 'running_total_credit')
def running_total_credit(journal_list):	
	sum=0
	for d in journal_list:
		sum+=d.Credit
	return sum