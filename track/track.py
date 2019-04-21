#!/env/bin python3

from conf import id
from colorama import init, Fore
from requests_xml import XML, XMLSession

init(autoreset=True)
session = XMLSession()


# TODO: Create main script with argparse
# TODO: Implement way to add username and password from config
# TODO: Add Colorama
# TODO: Integrate with UPS and FedEx
# TODO: Add more comments
# TODO: Code refactor?
# TODO: Look into testing errors


class Track:

    def __init__(self, tracking_number):
        self.tracking_number = tracking_number
        self.user_id = id['username']
        self.result = self.api_call()

    def api_call(self):
        """Calls the USPS API with the appropriate id and recieved Tracking
           number"""

        api_url = f"http://production.shippingapis.com/ShippingAPI.dll?API=\
        TrackV2&XML=<TrackRequest USERID='{self.user_id}'>\
        <TrackID ID='{self.tracking_number}'></TrackID></TrackRequest>"

        error = Fore.RED + 'Error occured connecting to API. Status code: s`tatus_code'

        r = session.get(api_url)
        if r.status_code != 200:
            print(error.replace(Fore.YELLOW + 'status_code', r.status_code))
        else:
            return r.xml

    def track_summary(self):
        """Returns the API Tracking Summary"""

        result = self.result.search('<TrackSummary>{}</TrackSummary>').pop()
        return result[0]

    def track_detail(self):
        """Returns the API Tracking Detail"""

        result = self.result.search('<TrackDetail>{}</TrackDetail>')
        return result

    def track_factory(self):
        """Combines the summary and detail into one return output"""

        print(Fore.WHITE + f"SUMMARY: {self.track_summary()}")
        print('DETAILS:')
        for i, items in enumerate(self.track_detail()):
            print(Fore.YELLOW + f"|-- {items[0]}")
