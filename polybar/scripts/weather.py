#!/usr/bin/env python3

# import libraries
import requests

with open("/home/ronit/.config/polybar/scripts/data.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

city = lines[0]
key = lines[1]
response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(
        city, key
    )
)
response.encoding = "utf-8"
j = response.json()
# get the data #
temp = j["main"]["temp"]
w_type = j["weather"][0]["main"]
icon = ""
desc = j["weather"][0]["main"]
if w_type == "Haze":

    icon = ""
elif w_type == "Clear":
    icon = ""
elif w_type == "Rain":
    icon = "歹"
elif w_type == "Thunderstorm":
    icon = "朗"
elif w_type == "Clouds":
    icon = "摒"
elif w_type == "Snow":
    icon = "流"
elif w_type == "Drizzle":
    icon = ""


# print the weather #
print(desc, "{}\N{DEGREE SIGN}C".format(temp))
