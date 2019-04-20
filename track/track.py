#!/env/bin python3

from requests_xml import XML, XMLSession

session = XMLSession()


class Track:

    def __init__(self, tracking_number):
        self.tracking_number = tracking_number
        self.result = self.api_call()

    def api_call(self):
        id = {'username': '', 'password': ''}
        api_sig = f'http://production.shippingapis.com/ShippingAPI.dll?API=TrackV2&XML=<TrackRequest USERID="{id["username"]}"><TrackID ID="{self.tracking_number}"></TrackID></TrackRequest>'
        r = session.get(api_sig)
        return r.xml

    def track_summary(self):
        result = self.result.search('<TrackSummary>{}</TrackSummary>').pop()
        return result[0]

    def track_detail(self):
        result = self.result.search('<TrackDetail>{}</TrackDetail>')
        return result

    def track_factory(self):

        print(f"SUMMARY: {self.track_summary()}")
        for i, items in enumerate(self.track_detail()):
            print(f"-- {items[0]}")
