from django.contrib.auth.forms import UsernameField
from django.http.response import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Agent, Lead
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


def landing_page(request):
    return render(request, 'leads/landing.html')


class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')


def lead_list(request):
    leads = Lead.objects.all()
    return render(request, "leads/page_one.html" ,context={
        "leads": leads
    })



def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    return render(request, 'leads/lead_detail.html', context={
        "lead": lead
    })


class LeadCreateView(generic.CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')

    
        



def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'leads/lead_create.html', context={
        "form": form
    })

    

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead) 
        if form.is_valid():
            form.save()
             
    return render(request, 'leads/lead_update.html', context={
        "lead": lead,
        "form": form
    })

def lead_delete(requet, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')


def lead_clear(request):
    lead = Lead.objects.all()
    lead.delete()
    return redirect('/leads')


