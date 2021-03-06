from mozls import query_mls, WifiNetwork, MLSException

from director.geo import Location
from director.geo.Provider import GeoProvider


class MozillaProvider(GeoProvider):
    def __init__(self, config):
        GeoProvider.__init__(self, config)

        self.api_key = config["mozilla"]["api_key"]

    def get_location(self, networks):
        try:
            mls_response = query_mls(
                wifi_networks=[WifiNetwork(mac_address=network["bssid"], signalStrength=int(network["signal"]))
                               for network in networks],
                apikey=self.api_key)
            return Location(mls_response.lat, mls_response.lon, accuracy=mls_response.accuracy, provider=self.provider)
        except MLSException:
            # handle MLS data as optional (it is anyway)
            return None
