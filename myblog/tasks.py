import logging
from django.core.mail import EmailMultiAlternatives
from django.template.context import Context
from django.template.loader import get_template
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from myblogger.celery import app

logger = logging.getLogger(__name__)

@app.task()
def send_email(data={}):
    from celery.contrib import rdb
    rdb.set_trace()
    if data.get('email', None):
        subject = data['sub']
        body = data['body']
        html = get_template(data['html']).render(Context(data))
        sender = 'verifyappmail@gmail.com'
        recipient = data['email']
        email = EmailMultiAlternatives(subject,
                                       body,
                                       from_email=sender,
                                       to=[recipient])
        email.attach_alternative(html, "text/html")
        email.send()
        logger.info("Email Sent")