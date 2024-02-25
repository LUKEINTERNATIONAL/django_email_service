from django.core.mail import send_mail, EmailMessage
from django.http import JsonResponse
from django.template import loader
from rest_framework.views import APIView
import datetime
from .models import Sentemails
from rest_framework import authentication, permissions
from rest_framework.pagination import PageNumberPagination
from .serializers import SentemailsSerializer
from django.core.mail.message import EmailMultiAlternatives

class CustomPagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = 'page_size'  # Query parameter to override page size
    max_page_size = 100  # Maximum page size allowed

class ContactView(APIView):
    def post(self, request):
        subject = request.data.get('subject')
        message = request.data.get('message')
        from_email = 'tams@linmalawi.org'
        recipient_email = request.data.get('recipient_email')
        
        if not subject or not message or not recipient_email:
            response_data = {'error': 'Missing required data'}
            return JsonResponse(response_data, status=400)
        
        # Split the recipient_email string into a list of email addresses
        recipient_list = [email.strip() for email in recipient_email.split(',')]

        try:
            # Load the email template
            email_template = loader.get_template('email_template.html')
            
            # Get the current year
            current_year = datetime.datetime.now().year
            
            # Render the email content with the provided data and current year
            email_content = email_template.render({'subject': subject, 'message': message, 'year': current_year})
            
            # Create an EmailMessage instance and send the email
            email = EmailMessage(subject, email_content, from_email, recipient_list)
            email.content_subtype = "html"  # Set the content type to HTML
            email.send()
            
            sentemail = Sentemails()
            sentemail.subject = request.data.get('subject')
            sentemail.recipient_email =  request.data.get('recipient_email')
            sentemail.save()
            
            response_data = {'message': 'Email sent successfully'}
            return JsonResponse(response_data)
        except Exception as e:
            error_message = str(e)
            response_data = {'error': error_message}
            return JsonResponse(response_data, status=400)
        
class GetSentEmails(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination

    def get(self, request):
        user = request.user
        sentemails = Sentemails.objects.filter()  # Fetch all user activities
        
        # Extract pagination parameters from the query string
        page = request.GET.get('page', None)
        page_size = request.GET.get('page_size', None)
        
        # Create a paginator instance with custom pagination class
        paginator = self.pagination_class()
        
        # Paginate the queryset using extracted page and page_size values
        paginated_queryset = paginator.paginate_queryset(sentemails, request)
        
        serializer = SentemailsSerializer(paginated_queryset, many=True)
        print(serializer.data)
        return paginator.get_paginated_response(serializer.data)
    
class EmailWithAttachmentsView(APIView):
    def post(self, request):
        subject = request.data.get('subject')
        message = request.data.get('message')
        from_email = 'tams@linmalawi.org'
        recipient_email = request.data.get('recipient_email')
        attachments = request.FILES.getlist('attachment_0')

        if not subject or not message or not recipient_email:
            response_data = {'error': 'Missing required data'}
            return JsonResponse(response_data, status=400)

        recipient_list = [email.strip() for email in recipient_email.split(',')]

        try:
            email = EmailMultiAlternatives(subject, message, from_email, recipient_list)
            email.content_subtype = "html"

            for attachment in attachments:
                email.attach(attachment.name, attachment.read(), attachment.content_type)

            email_template = loader.get_template('email_template.html')
            current_year = datetime.datetime.now().year
            email_content = email_template.render({'subject': subject, 'message': message, 'year': current_year})

            email.attach_alternative(email_content, "text/html")
            email.send()

            sentemail = Sentemails()
            sentemail.subject = subject
            sentemail.recipient_email = recipient_email
            sentemail.save()

            response_data = {'message': 'Email sent successfully'}
            return JsonResponse(response_data)
        except Exception as e:
            error_message = str(e)
            response_data = {'error': error_message}
            return JsonResponse(response_data, status=400)
        
