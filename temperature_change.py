import requests 

api_key = "219b74026949c164fc504f625a7b805c"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ") 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
response = requests.get(complete_url) 
x = response.json() 


if (x["cod"] != "404"): 
    y = x["main"]
    current_temperature_kelvin = y["temp"]
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]

    temp_fahrenheit = round((current_temperature_kelvin - 273.15) * 9/5 + 32)
    temp_celcius = round(current_temperature_kelvin - 273.15)
    print(" Temperature (in fahrenheit unit) = " + str(temp_fahrenheit))
    print(" Temperature (in celcius unit) = " + str(temp_celcius))
    print(" Temperature (in kelvin unit) = " + str(current_temperature_kelvin) 
    + "\n atmospheric pressure (in hPa unit) = " + str(current_pressure) 
    + "\n humidity (in percentage) = " + str(current_humidiy) 
    + "\n description = " + str(weather_description))
else:
    print(" City Not Found ")
