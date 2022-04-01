"""Platform for sensor integration."""

import logging
#from datetime import timedelta
#import json
#import requests
#import voluptuous as vol

"""from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
import homeassistant.helpers.config_validation as cv
from homeassistant.const import (CONF_API_KEY, CONF_LATITUDE, CONF_LONGITUDE, CONF_SCAN_INTERVAL)
from homeassistant.util import Throttle
from homeassistant.helpers.entity import Entity"""


from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import TEMP_CELSIUS
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

_LOGGER = logging.getLogger(__name__)

"""
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_API_KEY): cv.string,
    vol.Required(CONF_LATITUDE): cv.string,
    vol.Required(CONF_LONGITUDE): cv.string,
    vol.Required(CONF_SCAN_INTERVAL): cv.positive_int
})

SCAN_PERIOD = timedelta(minutes=15)

SENSORS = {
    'co': ['Carbon monoxide (CO)', 'μg/m3', 'mdi:molecule-co'],
    'h': ['Humidity', 'RH%', 'mdi:water-percent'],
    'no2': ['Nitrogen dioxide (NO2)', 'μg/m3', 'mdi:smog'],
    'o3': ['Ozone (O3)', 'μg/m3', 'mdi:skull-outline'],
    'p': ['Atmospheric pressure', 'hPa', 'mdi:gauge'],
    'pm10': ['Coarse particles (PM10)', 'μg/m3', 'mdi:grain'],
    'pm25': ['Fine particles (PM2.5)', 'μg/m3', 'mdi:grain'],
    'so2': ['Sulphur dioxide (SO2)', 'μg/m3', 'mdi:smog'],
    't': ['Temperature', 'degC', 'mdi:thermometer'],
    'w': ['Wind speed', 'm/s', 'mdi:weather-windy'],
    'aqi': ['Air Quality Index', '', 'mdi:leaf']
}"""

def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    #Set up the sensor platform.
    add_entities([WaqiSensor()])

"""def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    #Set up the sensor platform.
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
    add_entities(result)"""


"""class WaqiHttpRequester(object):

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
"""

class WaqiSensor(SensorEntity):
    #Representation of a Sensor.

    _attr_name = "Air Quality Index"
    _attr_device_class = SensorDeviceClass.AQI
    _attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        #Fetch new state data for the sensor.
        #This is the only method that should fetch new data for Home Assistant.
        self._attr_native_value = 23

"""class WaqiSensor(Entity):
    #Representation of a Sensor.

    def __init__(self, data, sensor_type):
        #Initialize the sensor.
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
        #Fetch new state data for the sensor.
        #This is the only method that should fetch new data for Home Assistant.
        
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
"""
