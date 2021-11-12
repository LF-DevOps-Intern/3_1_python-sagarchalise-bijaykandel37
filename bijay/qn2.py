#!/usr/bin/python3
import requests

#this part of code downloads a photo from the link into the filename mentioned below: i.e. ViratKohli.png
response = requests.get("https://www.bollywoodhungama.com/wp-content/uploads/2021/08/Virat-Kohli-opens-up-about-his-first-meeting-with-Anushka-Sharma-says-%E2%80%9CI-was-joking-around-with-her-and-that-really-connected%E2%80%9D-2.jpg")
file = open("ViratKohli.png", "wb")
file.write(response.content)
file.close()

#this part of code downloads a html page and saves locally
responses = requests.get("https://www.cricbuzz.com/profiles/1413/virat-kohli")
file = open("ViratKohli.html", "wb")
file.write(responses.content)
file.close()