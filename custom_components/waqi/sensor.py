"""Platform for sensor integration."""

import logging
import json
import requests

from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.util import Throttle
from homeassistant.helpers.entity import Entity
from .const import SENSORS, SCAN_PERIOD


_LOGGER = logging.getLogger(__name__)




def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the sensor platform."""
    lat = config.get(CONF_LATITUDE)
    lng = config.get(CONF_LONGITUDE)
    apikey = config.get(CONF_API_KEY)
    scanPeriod = config.get(CONF_SCAN_INTERVAL)

    try:
        data = WaqiHttpRequester(lat, lng, apikey, scanPeriod)
    except requests.exceptions.HTTPError as error:
        _LOGGER.error(error)
        return False

    result = []
    for res in SENSORS:
        result.append(WaqiSensor(data, res.lower()))
    add_entities(result)


class WaqiHttpRequester(object):

    def __init__(self, lat, lng, apikey, scanPeriod):
        self._state = None
        self.lat = lat
        self.lng = lng
        self.apikey = apikey
        self.scanPeriod = scanPeriod
        self.data = None

    @Throttle(SCAN_PERIOD)
    def update(self, sensorType):
        _LOGGER.debug("Updating WAQI sensors")
        try:
            self.data = json.loads("{" + requests.get(f"https://api.waqi.info/feed/geo:{self.lat};{self.lng}/?token={self.apikey}").text + "}")
        except requests.exceptions.RequestException as exc:
            _LOGGER.error("Error occurred while fetching data: %r", exc)
            self.data = None
            return False


class WaqiSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self, data, sensor_type):
        """Initialize the sensor."""
        self.data = data
        self.type = sensor_type
        self._unit = SENSORS[self.type][1]
        self._icon = SENSORS[self.type][2]
        self._state = None
        self._extra_state_attributes = None

    @property
    def name(self):
        return self._name

    @property
    def icon(self):
        return self._icon

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def extra_state_attributes(self):
        return self._extra_state_attributes

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        self.data.update(self.type)

        inputData = self.data.data

        try:

            if self.type == 'co':
                self._state = float(inputData["data"]["iaqi"]["co"]["v"])

            elif self.type == 'h':
                self._state = float(inputData["data"]["iaqi"]["h"]["v"])

            elif self.type == 'no2':
                self._state = float(inputData["data"]["iaqi"]["no2"]["v"])

            elif self.type == 'o3':
                self._state = float(inputData["data"]["iaqi"]["o3"]["v"])

            elif self.type == 'p':
                self._state = float(inputData["data"]["iaqi"]["p"]["v"])

            elif self.type == 'pm10':
                self._state = float(inputData["data"]["iaqi"]["pm10"]["v"])

            elif self.type == 'pm25':
                self._state = float(inputData["data"]["iaqi"]["pm25"]["v"])

            elif self.type == 'so2':
                self._state = float(inputData["data"]["iaqi"]["so2"]["v"])

            elif self.type == 't':
                self._state = float(inputData["data"]["iaqi"]["t"]["v"])

            elif self.type == 'w':
                self._state = float(inputData["data"]["iaqi"]["w"]["v"])

        except ValueError:
            self._state = None
