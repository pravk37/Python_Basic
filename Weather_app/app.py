import requests

def celsius_to_fahrenheit(celsius):
    # Function to convert temperature from Celsius to Fahrenheit
    return (celsius * 9/5) + 32

city = input("Enter the name of the City: ")
if not city:
    print('Please enter a valid city name!')
    exit()

unit = int(input("Choose the temperature unit(1 for Celsuis or 2 for Fahrenheit): "))

api_key = '71d0464993496732cc75c612f51b35c7'
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    try:
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        temperature = temperature - 273.15
        if unit == 1:
            unit = 'Celsius'
        elif unit == 2:
            temperature = celsius_to_fahrenheit(temperature)
            unit = 'Fahrenheit'
        else:
            print("Invalid Unit")
            exit()
        print(f'The temperature in {city} is {temperature:.2f} {unit} and the weather is described as {description}.')

    except KeyError:
        print("Unexpected data foramt received. Cannot process the weather information.")
    except Exception as e:
        print(f"An error occured: {e}")

elif response.status_code == 404:
    print("City not found. Please check the city name and try again")
else:
    print("Failed to retrieve data due to network error! Please try again later!!")
