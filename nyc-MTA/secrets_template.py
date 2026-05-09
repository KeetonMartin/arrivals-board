# This file is where you keep secret settings, passwords, and tokens!
# If you put them in the code you risk committing that info or sharing it

secrets = {
    "ssid": "",  # wifi network name
    "password": "",  # wifi password
    "timezone": "",  # http://worldtimeapi.org/timezones
    "openweather_key": "",  # api key from https://openweathermap.org/api
    "iqair_key": "",  # api key from https://www.iqair.com/us/air-quality-monitors/api
    "aio_username": "",  # username from https://accounts.adafruit.com/users/sign_in
    "aio_key": "",  # adafruit key
    "latitude": "",  # latitude where unit is located
    "longitude": "",  # latitude where unit is located
    "transit_url": "",  # url to your api endpoint on pythonganywhere or other host e.g. https://YOURUSERNAME.pythonanywhere.com/api/mta-arrivals
    "transit_headers": [
        {
            "api-key": "",  # api key for Flask app
            "station-ids": "",  # required, find ids in the stops.txt from http://web.mta.info/developers/data/nyct/subway/google_transit.zip
            "subway-lines": "",
        }  # Subway lines to be displayed, separated by a comma and no spaces
    ],
    "arrival_minimums": {
        "638N": 2,  # Hide Spring St uptown arrivals 2 minutes away or less
        "638S": 2,  # Hide Spring St downtown arrivals 2 minutes away or less
        "D21N": 3,  # Hide Broadway-Lafayette uptown arrivals 3 minutes away or less
        "D21S": 3,  # Hide Broadway-Lafayette downtown arrivals 3 minutes away or less
        "R22N": 3,  # Hide Prince St uptown arrivals 3 minutes away or less
        "R22S": 3,  # Hide Prince St downtown arrivals 3 minutes away or less
    },
    "default_direction": "North",
}  # For multiple stations, add an additional dictionary to this list
