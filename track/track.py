#!/env/bin python3

from requests_xml import XML, XMLSession
from conf import id

session = XMLSession()


# TODO: Create main script with argparse
# TODO: Implement way to add username and password from config
# TODO: Add Colorama
# TODO: Integrate with UPS and FedEx
# TODO: Add more comments
# TODO: Code refactor?


class Track:

    def __init__(self, tracking_number):
        self.tracking_number = tracking_number
        self.user_id = '639MARGR6822'
        self.result = self.api_call()

    def api_call(self):
        api_url = f"http://production.shippingapis.com/ShippingAPI.dll?API=\
        TrackV2&XML=<TrackRequest USERID='{self.user_id}'>\
        <TrackID ID='{self.tracking_number}'></TrackID></TrackRequest>"

        error = 'Error occured connecting to API. Status code: status_code'

        r = session.get(api_url)
        if r.status_code != 200:
            print(error.replace('status_code', r.status_code))
        else:
            return r.xml

    def track_summary(self):
        result = self.result.search('<TrackSummary>{}</TrackSummary>').pop()
        return result[0]

    def track_detail(self):
        result = self.result.search('<TrackDetail>{}</TrackDetail>')
        return result

    def track_factory(self):

        print(f"SUMMARY: {self.track_summary()}")
        print('DETAILS:')
        for i, items in enumerate(self.track_detail()):
            print(f"|-- {items[0]}")
