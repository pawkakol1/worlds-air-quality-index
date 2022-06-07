"""The worlds_air_quality_index component."""
from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import (
    callback,
    HomeAssistant
)
from homeassistant.helpers.entity_registry import async_migrate_entries
from homeassistant.const import (
    CONF_NAME,
    CONF_LATITUDE, 
    CONF_LONGITUDE, 
    CONF_TOKEN,
    CONF_LOCATION,
    CONF_METHOD,
    CONF_ID
)

from .const import (
    PLATFORMS,
    GEOGRAPHIC_LOCALIZATION
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up World's Air Quality Index from a config entry."""

    hass.config_entries.async_setup_platforms(entry, PLATFORMS)
    entry.async_on_unload(entry.add_update_listener(update_listener))
    return True


async def update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Handle options update."""
    await hass.config_entries.async_reload(entry.entry_id)


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload worlds_air_quality_index config entry."""

    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

async def async_migrate_entry(hass, config_entry):
    """Migrate worlds_air_quality_index old entry."""
    _LOGGER.debug("Migrating from version %s", config_entry.version)

    
    #  Flatten configuration but keep old data if user rollbacks HASS prior to 0.106
    if config_entry.version == 1:
        _LOGGER.info(config_entry.data)

    

    return True