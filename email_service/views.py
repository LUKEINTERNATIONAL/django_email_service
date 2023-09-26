from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail

class ContactView(View):
    template_name = 'email_service/contact.html'
    success_template_name = 'email_service/success.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        subject = request.POST['subject']
        message = request.POST['message']
        from_email = 'your_email@gmail.com'
        recipient_list = [request.POST['recipient_email']]

        send_mail(subject, message, from_email, recipient_list)
        return render(request, self.success_template_name)

