import requests

class Weatherstack:
    def __init__(self, api_key):
        """
        Initializes the weatherstack object using the API key

        Args:
            api_key (str): key to access the API
        """
        self.api_key = api_key
        self.api_url = "http://api.weatherstack.com/current"
        
    def __str__(self):
        """
        Returns the url to the API

        Returns:
            str: weatherstack API url
        """
        return f"WeatherStack API: {self.api_url}"

    def get(self, location):
        """
        Fetches the current weather info of the specified location inside the API

        Args:
            location (str): location where the user wants to look at the weather information

        Returns:
            dict: dictionary of all the information retrieved from the API
        """
        params = {
            "access_key": self.api_key,
            "query": location
        }

        r = requests.get(self.api_url, params=params)
        response = r.json()
        return response