# worlds-air-quality-index

A Home Assistant custom Integration for World's Air Quality Index (waqi.info).

Integration supports below sensors of WAQI station:

- Air Quality Index
- Particulate matter (PM10)
- Particulate matter (PM2,5)
- Carbon monoxide (CO)
- Nitrogen dioxide (NO2)
- Ozone (O3)
- Sulphur dioxide (SO2)
- Humidity
- Atmospheric pressure
- Temperature
- Rain
- Wind speed

It use geolocalized coordinates of station only.

# Installation

Copy worlds_air_quality_index folder into /config/custom_components of Home Assistant instance.
You can also use HACS to install this repository.

# Adding Integration

To add integration use "Add Integration" of Home Assistant UI, and choose "World's Air Quality Index".
In popup window put:

- your waqi.info account token (required)
- your own name of station (optional)
- latitude of WAQI station (optional)
- longitude of WAQI station (optional)

To get WAQI token you need to sign up on waqi.info.
If you won't put geolocalized coordinates of station, it will take your home coordinates, and it will find the clostest station.
If you won't put your own name it will take name of found station.

You can add more than 1 station.

Diffrent stations support diffrent data, "World's Air Quality Index" integration will recognise all parameters according to list of integration's supported sensors.
