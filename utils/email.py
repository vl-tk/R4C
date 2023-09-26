from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import Template
from django.template.loader import get_template


def __send_mail(
    plaintext: Template,
    html: Template,
    to_emails,
    context=None,
    subject="Info",
    from_email=settings.EMAIL_FROM,
):
    if context is None:
        context = {}

    text_content = plaintext.render(context)
    html_content = html.render(context)
    msg = EmailMultiAlternatives(
        subject=subject, body=text_content, from_email=from_email, to=to_emails
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_waiting_list_email(emails, model, version):
    __send_mail(
        plaintext=get_template("emails/waiting_list_item_available.txt"),
        html=get_template("emails/waiting_list_item_available.txt"),
        context={"model": model, "version": version},
        subject="Уведомление о появлении модели робота",
        to_emails=emails,
    )
