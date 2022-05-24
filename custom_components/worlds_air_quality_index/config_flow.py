"""Adds config flow for worlds_air_quality_index integration."""
from __future__ import annotations

from typing import Any

from .waqi_api import WaqiDataRequester

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult
import homeassistant.helpers.config_validation as cv

from homeassistant.const import (
    CONF_NAME,
    CONF_LATITUDE, 
    CONF_LONGITUDE, 
    CONF_TOKEN
)
from .const import (
    DOMAIN,
    DEFAULT_NAME
)

DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_TOKEN): cv.string,
        vol.Optional(CONF_NAME): cv.string,
        vol.Optional(CONF_LATITUDE): cv.string,
        vol.Optional(CONF_LONGITUDE): cv.string,
    }
)


class WorldsAirQualityIndexConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for worlds_air_quality_index integration."""

    VERSION = 1

    async def async_step_import(self, config: dict[str, Any]) -> FlowResult:
        """Import a configuration from config.yaml."""

        name = config.get(CONF_NAME, DEFAULT_NAME)
        self._async_abort_entries_match({CONF_NAME: name})
        config[CONF_NAME] = name
        return await self.async_step_user(user_input=config)

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""

        errors = {}

        if user_input:

            token = user_input[CONF_TOKEN]
            latitude = user_input.get(CONF_LATITUDE, self.hass.config.latitude)
            longitude = user_input.get(CONF_LONGITUDE, self.hass.config.longitude)
            requester = WaqiDataRequester(latitude, longitude, token)
            await self.hass.async_add_executor_job(requester.update)

            testData = requester.GetData()
            stationName = requester.GetStationName()
            name = user_input.get(CONF_NAME, stationName)

            if testData is None:
                errors["base"] = "invalid_token"
            elif stationName is None:
                errors["base"] = "invalid_station_name"
            else:
                await self.async_set_unique_id(name)
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=name,
                    data={
                        CONF_NAME: name,
                        CONF_TOKEN: token,
                        CONF_LATITUDE: latitude,
                        CONF_LONGITUDE: longitude,
                    },
                )

        return self.async_show_form(
            step_id="user",
            data_schema=DATA_SCHEMA,
            errors=errors,
        )
    

