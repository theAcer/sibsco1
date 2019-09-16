import re
import nexmo
import africastalking


class Sms:
    def __init__(self, phonenumber, message):
        self.service_url = u"http://{Provider's endpoint}"
        self.headers = {
            'Content-type': 'application/json',
            'Accept': 'text/plain',
            'User-Agent': 'mySms/1 (+https://Samsonnjogu.com)'
        }
        self.Phonenumber = phonenumber
        self.Message = message


    @staticmethod
    def _checkDate(datetime=None):

        if re.match(r'\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}', datetime):
            return datetime
        return None

    @staticmethod
    def _checkPhone(phone):
        phonePattern = re.compile(r'(^254[0-9]+)$', re.VERBOSE)
        return phone is not None and phonePattern.search(phone)

    @staticmethod
    def _checkSender(sender):
        regxPattern = re.compile(r'^[0-9]+}$', re.VERBOSE)
        return sender


class NexmoProvider:
    def __init__(self, phonenumber, message):
        self.api = '094275bd'
        self.secret = 'cz2dfC1A27kpjbkX'

    def send_sms(self, phone , msg ):
        client = nexmo.Client(key=self.api, secret=self.secret)
        responseData = client.send_message({
            'from': 'Nexmo',
            'to': phone,
            'text': msg,
        })
        if responseData["messages"][0]["status"] == "0":
            return ("Message sent successfully.")
        else:
            return (f"Message failed with error: {responseData['messages'][0]['error-text']}")

class AfricastalkingProvider:
    def __init__(self, phonenumber, message):
        self.api = '0f2dccac996fc26c0b80b1418e71dfb6fb4b8fa8a6f5c669847067069af9d10b'
        self.username = 'sandbox'
        self.Phone = phonenumber
        self.Msg = message

        self.sms = Sms(phonenumber, message)
    def send_sms(self, phone, msg):
        africastalking.initialize(self.username, self.api)
        # Get the SMS service
        sms = africastalking.SMS
        # Define some options that we will use to send the SMS
        recipients = [phone]
        message = msg
        sender = '6434'
        try:
            # Once this is done, that's it! We'll handle the rest
            response = sms.send(message, recipients, sender)
            return (response)
        except Exception as e:
            print(f"Houston, we have a problem {e}")





