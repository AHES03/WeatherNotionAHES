import requests


# Replace with your OpenWeatherMap API key
API_KEY = '969defe4841750d470f3e909b6eddfef'

# API endpoint URL for current weather by city name
url = f'http://api.openweathermap.org/data/2.5/weather'

# Define the city name for which you want to fetch weather
city_name = 'London'

# Define query parameters
params = {
    'q': city_name,
    'appid': API_KEY,
    'units': 'metric'  # Use 'imperial' for Fahrenheit
}
response = requests.get(url, params=params)
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract relevant weather information
    temperature = data["main"]["temp"]
    weather_description = data["weather"][0]["description"]

    print(f"Temperature: {temperature}°C")
    print(f"Description: {weather_description}")
    html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Weather Report</title>
        </head>
        <body>
            <h1>Weather Report for {city_name}</h1>
            <p>Temperature: {temperature}°C</p>
            <p>Weather Description: {weather_description}</p>
        </body>
        </html>
        """

    # Save the HTML content to a file
    with open('index.html', 'w') as html_file:
        html_file.write(html_content)

    print("HTML weather report generated.")
else:
    print(f"API request failed with status code: {response.status_code}")


