key = "219b74026949c164fc504f625a7b805c"
url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
complete_url = url + "appid=" + key + "&q=" + city_name
response = requests.get(complete_url)


data = response.json()


if data["cod"] != "404":
    base = data["main"]
    current_temperature = base["temp"]
    current_pressure = base["pressure"]
    current_humidiy = base["humidity"]
    weather = data["weather"]
    weather_description = weather[0]["description"]
    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description))

else:
    print(" City Not Found ") 
