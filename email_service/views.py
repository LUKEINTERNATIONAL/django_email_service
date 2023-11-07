from django.core.mail import send_mail, EmailMessage
from django.http import JsonResponse
from django.template import loader
from rest_framework.views import APIView
import datetime

class ContactView(APIView):
    
    def post(self, request):
        subject = request.data.get('subject')
        message = request.data.get('message')
        from_email = 'dominickasanga@gmail.com'
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
            
            response_data = {'message': 'Email sent successfully'}
            return JsonResponse(response_data)
        except Exception as e:
            error_message = str(e)
            response_data = {'error': error_message}
            return JsonResponse(response_data, status=400)
