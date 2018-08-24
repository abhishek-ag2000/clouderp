from django import template

register = template.Library()

@register.filter(name= 'running_total')
def running_total(journal_details):
	return sum(d.Debit for d in journal_details)


@register.filter(name= 'running_total_credit')
def running_total_credit(journal_details):
	#return sum(d.Credit for d in journal_list)
	sum=0
	for d in journal_details:
		sum+=d.Credit
	return sum