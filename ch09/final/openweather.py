import requests

class OpenWeather:
    def __init__(self):
        """
        Initializes the openweather object
        """
        self.api_url = "https://api.openweathermap.org/data/2.5/weather"
        
    def __str__(self):
        """
        Returns the url to the API

        Returns:
            str: openweather API url
        """
        return f"Weather API: {self.api_url}"

    def get(self, city):
        """
        Retrieves the current weather information for the location given 

        Args:
            city (str): location that the user entered to view the weather 

        Returns:
            dict: dictionary of all the information from the openweather API
        """
        params = {
            'q': city,
            'appid': 'c41ffa76ad933d54e4f702b5778c539f',
            'units': 'imperial'
        }

        r = requests.get(self.api_url, params=params)
        response = r.json()
        
        return response