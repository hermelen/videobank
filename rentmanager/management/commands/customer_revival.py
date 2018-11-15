from django.core.management.base import BaseCommand

from rentmanager.models import MovieRent

from datetime import datetime, timedelta

from tzlocal import get_localzone # pip install tzlocal

from django.core.mail import EmailMultiAlternatives

from videobank.extra_settings import EMAIL_HOST_USER

from django.utils import translation






class Command(BaseCommand):
    help = "Contact customer that are late"

    def handle(self, *args, **options):
        translation.activate('en')
        local_tz = get_localzone()   # get local timezone
        dead_line = datetime.now(local_tz) - timedelta(minutes=20)
        late_rents = MovieRent.objects.filter(checkout_date__lte=dead_line)

        for late_rent in late_rents:
            customerMail = late_rent.customer.user.email
            customerName = late_rent.customer.user.username
            filmName     = late_rent.movies.title
            rentDate     = late_rent.checkout_date
            txt_message = 'Hi '+ customerName.capitalize() + '(' + customerMail + ')' +' you rented "' + filmName.capitalize() + '". You keep it too long, please return it fast!'


            subject, from_email, to = 'VideoBank', EMAIL_HOST_USER, customerMail
            text_content = txt_message
            html_content = '<p>This is an <strong>important</strong> message.</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            msg.send()

            # rentDuration = datetime.now() - rentDate
