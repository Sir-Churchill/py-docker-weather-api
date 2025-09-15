import os
import requests

URL = "https://api.weatherapi.com/v1/current.json?"
FILTER = "Paris"

API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(URL + f"key={API_KEY}&q={FILTER}")
    if response.status_code == 200:
        data = response.json()

        print(f"{data["location"]["name"]}/{data["location"]["country"]} "
              f"{data["location"]["localtime"]} "
              f"Weather: {data["current"]["temp_c"]} Celsius, "
              f"{data["current"]["condition"]["text"]}")
    else:
        print("Error:", response.status_code, response.text)


if __name__ == "__main__":
    get_weather()
