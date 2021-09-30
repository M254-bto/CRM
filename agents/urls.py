from django.urls import path
from .views import agent_delete, agent_detail, agent_list, AgentCreateView

app_name = 'agents'


urlpatterns = [
    path('', agent_list, name='agent-list'),
    path('create/', AgentCreateView.as_view(), name='agent-create'),
    path('<int:pk>/', agent_detail, name='agent-detail'),
    path('<int:pk>/delete/', agent_delete, name='agent-delete'),
    path('clear/', agent_delete, name='agent-clear'),
    
]