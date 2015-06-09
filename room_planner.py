from flask import Flask
from pytz import timezone
from datetime import datetime


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

from pyexchange import Exchange2010Service, ExchangeNTLMAuthConnection
def connect():

    URL = 'https://exchange.williaminc.com/EWS/Exchange.asmx'
    USERNAME = 'william\\pgranger'
    PASSWORD = "xxx"
    connection = ExchangeNTLMAuthConnection(url=URL,
                                            username=USERNAME,
                                            password=PASSWORD)
    service = Exchange2010Service(connection)
    events = service.calendar().list_events(
        start=timezone("America/Montreal").localize(datetime(2015, 6, 1, 8, 0, 0)),
        end=timezone("America/Montreal").localize(datetime(2015, 6, 10, 11, 0, 0)),
        details=True
    )

    import ipdb; ipdb.set_trace()
    for event in events.events:
        print ("{start} {stop} - {subject}".format(
            start=event.start,
            stop=event.end,
            subject=event.subject
        ))


@app.route('/')
def home():

    connect()
    return 'Home'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
