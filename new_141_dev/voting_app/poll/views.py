from django.shortcuts import render, redirect, get_object_or_404
from .models import Poll
from .forms import VoteForm

def vote_view(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    form = VoteForm()

    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['choice']
            if choice == '1':
                poll.votes_1 += 1
            elif choice == '2':
                poll.votes_2 += 1
            elif choice == '3':
                poll.votes_3 += 1
            poll.save()
            return redirect('results', poll_id=poll.id)

    return render(request, 'poll/vote.html', {'poll': poll, 'form': form})

def results_view(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    return render(request, 'poll/results.html', {'poll': poll})
def home_view(request):
    return render(request, 'poll/home.html')
from django.shortcuts import render

def poll_list_view(request):
    polls = Poll.objects.all()
    return render(request, 'poll/poll_list.html', {'polls': polls})

