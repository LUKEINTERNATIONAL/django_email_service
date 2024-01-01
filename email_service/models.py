from django.db import models

class Sentemails(models.Model):
    subject = models.TextField()
    recipient_email = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
