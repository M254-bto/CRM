from django.shortcuts import reverse, render, redirect
from leads.models import Agent
from django.views import generic
from .forms import AgentCreateForm
from django.shortcuts import reverse



#list view

def agent_list(request):
    agents = Agent.objects.all()
    context = {
        "agents": agents
    }
    return render(request, 'agents/agent-list.html', context)



#create view

class AgentCreateView(generic.CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentCreateForm


    def get_success_url(self):
        return reverse('agents:agent-list')
 
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)


def agent_detail(request, pk):
    agents = Agent.objects.get(id=pk)
    return render(request, 'agents/agent_detail.html', context = {
        "agents": agents
    })



def agent_delete(request, pk):
    agent = Agent.objects.get(id=pk)
    agent.delete()
    return redirect(request, 'agents:agent-list')


def agent_clear(request):
    agents = Agent.objects.all()
    agents.delete()
    
    return redirect('agents:agent-list')