"""Constants for the World Air Quality Index integration."""

from datetime import timedelta

from typing import Final

from homeassistant.const import (
    UnitOfPressure,
    UnitOfSpeed,
    UnitOfTemperature,
    UnitOfLength,
    PERCENTAGE,
    Platform
)
from homeassistant.components.sensor import SensorDeviceClass

DOMAIN = "worlds_air_quality_index"
PLATFORMS = [Platform.SENSOR]
SW_VERSION = "1.1.0"

DEFAULT_NAME = 'waqi1'
DISCOVERY_TYPE = "discovery_type"
GEOGRAPHIC_LOCALIZATION = "Geographic localization"
SCAN_INTERVAL = timedelta(minutes=30)
STATION_ID = "Station ID"

SENSORS = {
    'aqi': ['Air Quality Index', ' ', 'mdi:leaf', SensorDeviceClass.AQI],
    'pm10': ['Particulate matter (PM10)', ' ', 'mdi:skull-outline', SensorDeviceClass.PM10],
    'pm25': ['Particulate matter (PM2.5)', ' ', 'mdi:skull-outline', SensorDeviceClass.PM25],
    'neph': ['Nephelometry', ' ', 'mdi:skull-outline', None],
    'co': ['Carbon monoxide (CO)', ' ', 'mdi:molecule-co', SensorDeviceClass.CO],
    'h': ['Humidity', PERCENTAGE, 'mdi:water-percent', SensorDeviceClass.HUMIDITY],
    'no2': ['Nitrogen dioxide (NO2)', ' ', 'mdi:smog', SensorDeviceClass.NITROGEN_DIOXIDE],
    'o3': ['Ozone (O3)', ' ', 'mdi:skull-outline', SensorDeviceClass.OZONE],
    'p': ['Atmospheric pressure', UnitOfPressure.HPA, 'mdi:gauge', SensorDeviceClass.PRESSURE],
    'so2': ['Sulphur dioxide (SO2)', ' ', 'mdi:smog', SensorDeviceClass.SULPHUR_DIOXIDE],
    't': ['Temperature', UnitOfTemperature.CELSIUS, 'mdi:thermometer', SensorDeviceClass.TEMPERATURE],
    'r': ['Rain', UnitOfLength.MILLIMETERS, 'mdi:weather-rainy', SensorDeviceClass.PRECIPITATION],
    'w': ['Wind speed', UnitOfSpeed.METERS_PER_SECOND, 'mdi:weather-windy', SensorDeviceClass.WIND_SPEED],
    'wg': ['Wind gust', UnitOfSpeed.METERS_PER_SECOND, 'mdi:weather-windy', SensorDeviceClass.WIND_SPEED],
    'uvi': ['UV Index', ' ', 'mdi:sun-wireless', None],
}
