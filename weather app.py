import requests

api_key = '.....'

def f_to_c(f):
    return round((f - 32) * 5/9)

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
)

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp_f = round(weather_data.json()['main']['temp'])
    temp_c = f_to_c(temp_f)

    print(f"The weather in {user_input} is: {weather}")
    print(f"Temperature: {temp_f}ºF / {temp_c}ºC")
