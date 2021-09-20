from django.urls import path
from leads.views import LeadCreateView, landing_page, lead_create, lead_delete, lead_detail, lead_list, lead_update, lead_clear


app_name = 'leads'

urlpatterns = [
    path('', landing_page, name='landing'),
    path('leads/',lead_list, name='lead-list'),
    path('<int:pk>/' , lead_detail, name='lead-detail'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('<int:pk>/update/' , lead_update, name='lead-update'),
    path('<int:pk>/delete/' , lead_delete, name='lead-delete'),
    path('clear/', lead_clear, name='lead-clear')
]