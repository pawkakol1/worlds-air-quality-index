import json
import requests
import logging
from homeassistant.util import Throttle
from .const import SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)

class WaqiDataRequester(object):

    def __init__(self, lat, lng, token):
        self._lat = lat
        self._lng = lng
        self._token = token
        self._data = None
        self._stationName = None
        self._stationIdx = None
        self._updateLastTime = None

    @Throttle(SCAN_INTERVAL)
    def update(self):
        _LOGGER.debug("Updating WAQI sensors")
  
        try:
            _dat = requests.get(f"https://api.waqi.info/feed/geo:{self._lat};{self._lng}/?token={self._token}").text
            self._data = json.loads(_dat)
            self._stationName = self._data["data"]["city"]["name"]
            self._stationName = self._stationName.replace(", ", "_").replace(" ", "_").replace("(", "").replace(")","").lower()
            self._stationIdx = self._data["data"]["idx"]
            self._updateLastTime = self._data["data"]["time"]["iso"]
        except requests.exceptions.RequestException as exc:
            _LOGGER.error("Error occurred while fetching data: %r", exc)
            self._data = None
            self._stationName = None
            return False
    
    def GetData(self):
        return self._data

    def GetStationName(self):
        return self._stationName
        
    def GetStationIdx(self):
        return self._stationIdx
        
    def GetUpdateLastTime(self):
        return self._updateLastTime
