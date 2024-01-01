from django.urls import path
from .views import ContactView, GetSentEmails

urlpatterns = [
    path('contact', ContactView.as_view(), name='contact'),
    path('get_sent_emails', GetSentEmails.as_view(), name='get_sent_emails')
]
