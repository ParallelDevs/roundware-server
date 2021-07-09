from roundware import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.mail.message import EmailMessage

class NotificationsEmails:

    from_email = 'cjamcu@gmail.com'



    def send_email_new_asset(to_email,to_username,asset_id):
        print("Sending email to: " + str(to_email))

        url_new_asset = settings.ROUNDWARE_SERVER_URL + "/rw/asset/{id}/change/".format(id=asset_id);

        mail = EmailMessage(
            from_email=NotificationsEmails.from_email,
            to=to_email)

        mail.template_id = 'd-b13af199d5c84d1ca110f68cdda7d97e'
        mail.dynamic_template_data = {  # Sendgrid v6+ only
            "username": to_username,
            "path_asset": url_new_asset
        }
    

        mail.send(fail_silently=False)
        

    def send_email_new_asset_published(to_email,author,asset_id):
        url_new_asset = settings.ROUNDWARE_SERVER_URL + "/rw/asset/{id}/change/".format(id=asset_id);
        mail = EmailMessage(
            from_email=NotificationsEmails.from_email,
            to=to_email)
        mail.template_id = 'd-9e26ce0688cf46638fe4ebcfa3c3972d'
        mail.dynamic_template_data = {  # Sendgrid v6+ only
            "username": author,
            "path_asset": url_new_asset
        }
        mail.send(fail_silently=False)



    