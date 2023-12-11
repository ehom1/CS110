from openweather import OpenWeather
from weatherstack import Weatherstack

def main():
    stack_key = "e9aef19008df40ce6836ecf0bd81a175"
    open_api = OpenWeather()
    stack_api = Weatherstack(stack_key)

    city = str(input("\nEnter a city to compare the weather between two APIs: "))
    weather_data = open_api.get(city)
    stack_data = stack_api.get(city)

    print(open_api)
    print(stack_api)

    print("\n---Weather Information with Open Weather API---\n")
    print(f"Location: {weather_data['name']}")

    temp_fahrenheit = weather_data['main']['temp']
    temp_celsius = (temp_fahrenheit - 32) * 5/9
    
    print(f"Temperature: {temp_fahrenheit}°F / {temp_celsius}°C")
    print(f"Condition: {weather_data['weather'][0]['description']}")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    print(f"Cloud Cover Percentage: {weather_data['clouds']['all']}%")
    print(f"Pressure: {weather_data['main']['pressure']} hPa")
        
    print("\n---Weather Information with WeatherStack API---\n")
    print(f"Location: {city}")
    print(f"Temperature: {stack_data['current']['temperature']}°C")
    print(f"Feels Like: {stack_data['current']['feelslike']}°C")
    print(f"Weather Description: {stack_data['current']['weather_descriptions'][0]}")
    print(f"Humidity: {stack_data['current']['humidity']}%")
    print(f"Wind Speed: {stack_data['current']['wind_speed']} km/h")
    print(f"Wind Direction: {stack_data['current']['wind_dir']}")
    print(f"Pressure: {stack_data['current']['pressure']} mb\n")
    
main()