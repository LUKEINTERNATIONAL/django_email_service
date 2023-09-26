from django.shortcuts import render, redirect
from django.views import View
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.http import JsonResponse

class ContactView(APIView):
    # template_name = 'email_service/contact.html'
    # success_template_name = 'email_service/success.html'

    def post(self, request):
        subject = request.data['subject']
        message = request.data['message']
        from_email = 'your_email@gmail.com'
        recipient_list = [request.data['recipient_email']]

        try:
            send_mail(subject, message, from_email, recipient_list)
            response_data = {'message': 'Email sent successfully'}
            return JsonResponse(response_data)
        except Exception as e:
            error_message = str(e)
            response_data = {'error': error_message}
            return JsonResponse(response_data, status=400)

