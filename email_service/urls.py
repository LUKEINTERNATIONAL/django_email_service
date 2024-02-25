from django.urls import path
from .views import ContactView, GetSentEmails, EmailWithAttachmentsView

urlpatterns = [
    path('contact', ContactView.as_view(), name='contact'),
    path('get_sent_emails', GetSentEmails.as_view(), name='get_sent_emails'),
    path('email_with_attachments', EmailWithAttachmentsView.as_view(), name='email_with_attachments'),
]
