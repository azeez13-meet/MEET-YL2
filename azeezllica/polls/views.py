from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Choice, Poll

def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	context = { 'latest_poll_list': latest_poll_list }
	return render(request, 'index.html', context)

def detail(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'detail.html', {'poll': poll})

def results(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'results.html', {'poll': poll})

def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'detail.html', {
			'poll': p,
			'error_message': "You didn't select a choice."
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()

	return HttpResponseRedirect(reverse('results', args=(p.id,)))
	return HttpResponse("You're voting on poll %s." % poll_id)

def my_page(request):
	return render(request, 'my_page.html')

def help(request):
	return render(request, 'help.html')

def about(request):
	return render(request, 'about.html')
