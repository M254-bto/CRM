from django import forms
from leads.models import Agent



class AgentCreateForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = 'user',