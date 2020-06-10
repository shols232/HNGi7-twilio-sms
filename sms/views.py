from django.http import HttpResponse
from twilio.rest import Client

account_sid = 'AC084b5641a2435e72c3e1e894cf57db18'
auth_token = '5900504d34f0a41ce842b2ab9c91af5a'


def send_sms(request):
    number = request.GET.get('number')
    sms = request.GET.get('sms')
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=f'{number}',
            from_='+2563443388',
            to=f"{sms}"
        )

    return HttpResponse(message.sid)
