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
- Wind gust
- Wind speed

Different stations support different data, "World's Air Quality Index" integration will recognise all parameters (available in station) according to list of integration's supported sensors.

If station's API supports forecast for pollution sensors (these on above list):

- Carbon monoxide (CO)
- Nitrogen dioxide (NO2)
- Ozone (O3)
- Particulate matter (PM10)
- Particulate matter (PM2,5)
- Sulphur dioxide (SO2)

Pollution sensors will update forecast, and it will be able to read as attributes of the sensor:

<img src="https://github.com/pawkakol1/worlds-air-quality-index/tree/main/readme_files/forecast.png" height="414">

If the station supports forecast of some pollution sensor, but it doesn't support actual value of this sensor, then the sensor will be also ceated. Its current state will be set to "UNAVAILABLE", but forecast will be able to read as the sensor attributes.

There are 2 supported integration methods:

- using geolocalized coordinates (it works with WAQI internal stations only),
- using station ID.

Notice: WAQI API supports 2 different methods of providing station ID. It depends on the station is internal WAQI station or downloaded from other source by their API. Internal stations need to put just a number of station ID (without @ char). For external stations it needs to put station ID number with 'A' char prefix. If you want to integrate some station using ID, but you don't know what method you need to use, you can always check it using web browser. You just need to copy one of below link, paste to the URL of web browser, change number of interested station, and paste your token instead {{token}}

`https://api.waqi.info/feed/@13837/?token={{token}}`
or
`https://api.waqi.info/feed/A254464/?token={{token}}`

Web browser will receive some data, if station is supported or "Unknown ID" message, if it doesn't, but one of above link types should work.

# Installation

Use HACS to install this repository.
You can also copy worlds_air_quality_index folder into /config/custom_components of Home Assistant instance, then restart HA.

# Adding Integration

To add integration use "Add Integration" button in section Settings->Devices&Services section, and choose "World's Air Quality Index".
In popup window choose method of station adding:

- using geographic localization (NOTICE: it works with WAQI internal stations only),
- using station ID (NOTICE: it works with all API types available in WAQI:
  - WAQI internal stations,
  - stations from CanAir.IO,
  - stations from Citizen Science project luftdaten.info.

In case of geographic localization, there will be shown next window, where you need to put:

- your waqi.info account token (required),
- latitude of WAQI station (required),
- longitude of WAQI station (required),
- your own name of station (optional).

In case of station ID, there will be shown next window, where you need to put:

- your waqi.info account token (required),
- ID of WAQI station (required) - WAQI Internal stations it is needed to put just a number (without @ char), for stations from other sources it needs to put 'A' char as a prefix(eg. A67564),
- your own name of station (optional).

To get WAQI token you need to sign up [here](https://aqicn.org/data-platform/token/).
As a default your home coordinates (set in HA) are put in latitude and longitude fields in geographic localization method. This integration will find the closest station, what is supported by waqi.info API.
If you won't put your own name it will take name of found station.
You can add more than 1 station.
