from app.models import Sponsorship
from code_sponsor.celery import app

from .models import Click, Impression


@app.task(ignore_result=True)
def record_impression(token, user_agent, ip_address):
    print("Recording impression for token: {0} ({1})".format(
        token, ip_address))
    sponsorship = Sponsorship.objects.get(token=token)
    impression = Impression(sponsorship=sponsorship)

    impression.property_id = sponsorship.property_id
    impression.sponsor_id = sponsorship.sponsor_id
    impression.user_agent = user_agent
    impression.ip_address = ip_address
    impression.is_bot = False  # TODO

    impression.save()


@app.task(ignore_result=True)
def record_click(token, user_agent, ip_address, referer):
    print("Recording click for token: {0} ({1})".format(
        token, ip_address))
    sponsorship = Sponsorship.objects.get(token=token)
    click = Click(sponsorship=sponsorship)

    click.property_id = sponsorship.property_id
    click.sponsor_id = sponsorship.sponsor_id
    click.user_agent = user_agent
    click.ip_address = ip_address
    click.referer = referer
    click.is_bot = False  # TODO

    click.save()
