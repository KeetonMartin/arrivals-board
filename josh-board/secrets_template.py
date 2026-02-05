# Josh's board - Bus arrivals configuration
# This file is where you keep secret settings, passwords, and tokens!

secrets = {
    "ssid": "",  # wifi network name
    "password": "",  # wifi password
    "timezone": "America/New_York",  # http://worldtimeapi.org/timezones
    "openweather_key": "",  # api key from https://openweathermap.org/api
    "iqair_key": "",  # api key from https://www.iqair.com/us/air-quality-monitors/api
    "aio_username": "",  # username from https://accounts.adafruit.com/users/sign_in
    "aio_key": "",  # adafruit key
    "latitude": "",  # latitude where unit is located
    "longitude": "",  # longitude where unit is located

    # Base URL for the API
    "transit_url": "https://KeetonMartin.pythonanywhere.com",

    # Bus arrivals configuration for 1st Ave & 34th St
    # Stop IDs (no eastbound M34 - they don't need it):
    #   403359 - M34-SBS Westbound (E 34 ST/1 AV -> Javits) [→ right arrow]
    #   403480 - M15 Northbound (1 AV/E 34 ST -> uptown) [↓ down arrow]
    #   405610 - M15 Southbound (2 AV/E 33 ST -> downtown) [↑ up arrow]
    "transit_headers": [
        {
            "api-key": "sunshine-cloud-river-mountain",
            "station-ids": "403359,403480,405610",
            "subway-lines": "M34+,M15+",
            "endpoint": "/api/mta-bus-arrivals"
        }
    ],
    "default_direction": "South"
}
