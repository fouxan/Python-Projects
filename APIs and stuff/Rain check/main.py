import requests
from twilio.rest import Client
import os

api_key = os.environ.get("OWM_APIKEY")
auth_token = os.environ.get("AUTH_TOKEN")
acc_sid = os.environ.get("ACC_SID")
LAT = 17.377270
LNG = 78.383728

weather_params = {
    "lat": LAT,
    "lon": LNG,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=weather_params)
response.raise_for_status()
data = response.json()

hourly_data_2days = data["hourly"]
hourly_data_1day = hourly_data_2days[:24] 

will_rain = False
rain_time = 0

for hour in hourly_data_1day:
    if hour["weather"][0]["main"] == 'Rain':
        will_rain = True
        break

        
if will_rain:
    client = Client(acc_sid, auth_token)
    message = client.messages \
                    .create(
                        body="Yo rain today. Get ☔.",
                        from_='+13612829117',
                        to='+919390017296'
                    )

    print(message.status)