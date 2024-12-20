import requests
import json

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city_name):
        try:
            # Build the request URL
            url = f"{self.base_url}?q={city_name}&appid={self.api_key}&units=metric"

            # Send a request to the API
            response = requests.get(url)

            # Check if the response is valid
            if response.status_code == 200:
                data = response.json()

                # Extract useful information
                weather = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"],
                    "humidity": data["main"]["humidity"],
                    "wind_speed": data["wind"]["speed"],
                }
                return weather
            elif response.status_code == 404:
                print("City not found. Please check the name and try again.")
                return None
            else:
                print("Error fetching weather data. Try again later.")
                return None

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def save_weather_to_file(self, weather_data, file_name="weather_data.txt"):
        try:
            with open(file_name, "w") as file:
                json.dump(weather_data, file, indent=4)
            print(f"Weather data saved to {file_name}")
        except Exception as e:
            print(f"Error saving data to file: {e}")

# Function to get user input and display weather
def main():
    print("Welcome to the Weather App!")
    print("This app is focused on cities in Africa, particularly Kenya.")
    api_key = input("Enter your OpenWeatherMap API Key: ")
    weather_app = WeatherApp(api_key)

    while True:
        print("\nExamples of cities: Nairobi, Mombasa, Kisumu, Nakuru, Eldoret.")
        city = input("Enter the city name (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Thank you for using the Weather App!")
            break

        weather = weather_app.get_weather(city)
        if weather:
            print("\nWeather Information:")
            print(f"City: {weather['city']}")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Description: {weather['description']}")
            print(f"Humidity: {weather['humidity']}%")
            print(f"Wind Speed: {weather['wind_speed']} m/s")

            # Save to file
            weather_app.save_weather_to_file(weather)
