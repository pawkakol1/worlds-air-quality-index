# worlds-air-quality-index

A Home Assistant custom Integration for World's Air Quality Index (waqi.info).

Integration supports below sensors of WAQI station:

- Air Quality Index
- Carbon monoxide (CO)
- Nitrogen dioxide (NO2)
- Ozone (O3)
- Particulate matter (PM10)
- Particulate matter (PM2,5)
- Sulphur dioxide (SO2)
- Atmospheric pressure
- Humidity
- Temperature
- Rain
- Wind speed

Diffrent stations support diffrent data, "World's Air Quality Index" integration will recognise all parameters (availible in station) according to list of integration's supported sensors.

There are 2 supported integration methods:

- using geolocalized coordinates,
- using station ID.

Notice: waqi.info API supports stations with IDs between 1 and 13837 only. If your station has ID greater than 13837 it won't be able to add using station ID method nor geolocalized coordinates method. waqi.info website shows (on map) much more stations, than are supported by waqi.info API. All others stations are integrated with WAQI map from others websites. In the future waqi.info API would be developed, and there would be more supported stations, you can always check if your station is supported. You just need to copy below link, paste to the URL of web browser, change number of interested station, and paste your token insted {{token}}

`https://api.waqi.info/feed/@13837/?token={{token}}`

Web browser will receive some data, if station is supported or "Unknown ID" message, if it doesn't.

# Installation

Use HACS to install this repository.
You can also copy worlds_air_quality_index folder into /config/custom_components of Home Assistant instance, then restart HA.

# Adding Integration

To add integration use "Add Integration" button in section Settings->Devices&Services section, and choose "World's Air Quality Index".
In popup window choose method of station adding:

- using geographic localization,
- using station ID.

In case of geographic localization, there will be shown next window, where you need to put:

- your waqi.info account token (required),
- latitude of WAQI station (required),
- longitude of WAQI station (required),
- your own name of station (optional).

In case of station ID, there will be shown next window, where you need to put:

- your waqi.info account token (required),
- ID of WAQI station (required) - 13837 is proper, @13837 is not proper,
- your own name of station (optional).

To get WAQI token you need to sign up [here](https://aqicn.org/data-platform/token/).
As a default your home coordinates (set in HA) are putten in latitude and longitude fields in geographic localization method. This integration will find the clostest station, what is supported by waqi.info API.
If you won't put your own name it will take name of found station.
You can add more than 1 station.
