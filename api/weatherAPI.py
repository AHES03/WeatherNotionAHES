import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

API_KEY = '969defe4841750d470f3e909b6eddfef'
API_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.get("/api/weather")
async def get_weather(cityName: str):
    params = {
        'q': cityName,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "city": cityName,
            "temperature": data['main']['temp'],
            "weatherDescription": data['weather'][0]['description']
        }
        return JSONResponse(content=weather_data)
    else:
        return JSONResponse(content={"error": "Failed to fetch weather data"}, status_code=500)
