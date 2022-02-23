import requests 
from django.conf import settings

class OpenWeather:
	def __init__(self, city : str):
		self.city = city
		self.weatherKey = settings.WEATHER_KEY
	
	def apiCall(self):
		apiURL = f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.weatherKey}&units=metric'
		print(apiURL)
		result = requests.get(apiURL)
		return result.json()

	def returnResult(self):
		apiResult = self.apiCall()
		print(apiResult)
		print(apiResult["cod"])
		if(apiResult["cod"] == 200):
			current_temp = apiResult["main"]["temp"]
			print("cod")
			print(current_temp)
		else:
			current_temp = None
		return{
			"city": self.city,
			"temprature": current_temp
		}