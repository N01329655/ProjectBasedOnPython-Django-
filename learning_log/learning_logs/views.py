from django.shortcuts import render


from django.http import HttpResponseRedirect, Http404
from django.urls import reverse



from .forms import TopicForm
from .models import Topic
from .forms import EntryForm
from .models import Entry

from django.contrib.auth.decorators import login_required 



# Create your views here.
def index(request):
	return render(request,'learning_logs/index.html')
	
	
	
@login_required
def topics(request):
	## to display topics only related to the logged user
	topics = Topic.objects.filter(own=request.user).order_by('date_added')
	context = {'topics' : topics}
	return render(request,'learning_logs/topics.html',context)
	
@login_required	
def topic(request,topic_id):
		## print out a topic retrieved by topic_id and all its entries
	topic = Topic.objects.get(id=topic_id)
	if topic.own != request.user:
		return Http404
	
	
	
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic':topic, 'entries':entries}
	return render(request,'learning_logs/topic.html',context)
	
@login_required	
def new_topic(request):
	## determine a new topic 
	if request.method != 'POST':
		## data is not been send; creating a new form 
		form = TopicForm()
	
	else:
		## Post data is been send; process data 
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.own = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))
	
	context = {'form' : form}
	return render(request,'learning_logs/new_topic.html',context)
	
@login_required	
def new_entry(request,topic_id):
	
	topic = Topic.objects.get(id=topic_id)
	
	if request.method != 'POST':
		form = EntryForm()
	
	else:
		form = EntryForm(data = request.POST)
		
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
			
	context = {'topic' : topic, 'form': form}
	return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	
	if topic.own != request.user:
		raise Http404
	

	if request.method != 'POST':
		form = EntryForm(instance=entry)
		
	else:
		form = EntryForm(instance=entry,data=request.POST)	
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
	
	
	context = {'entry':entry,'topic':topic,'form':form}
	return render(request,'learning_logs/edit_entry.html',context)
	
	
	
	
	
	
	
	
	
		
	
