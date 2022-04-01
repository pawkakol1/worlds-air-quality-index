"""Constants for the World's Air Quality Index integration."""

from datetime import timedelta
from homeassistant.components.sensor import PLATFORM_SCHEMA
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.const import (CONF_API_KEY, CONF_LATITUDE, CONF_LONGITUDE, CONF_SCAN_INTERVAL)

# This is the internal name of the integration, it should also match the directory
# name for the integration.

DOMAIN = "waqi"

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
}

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_API_KEY): cv.string,
    vol.Required(CONF_LATITUDE): cv.string,
    vol.Required(CONF_LONGITUDE): cv.string,
    vol.Required(CONF_SCAN_INTERVAL): cv.positive_int
})