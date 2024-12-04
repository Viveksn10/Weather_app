from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        # Correctly format the API URL without spaces
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=e315ba08319f732654a0b9b40268ae42'

        try:
            # Fetch JSON data from the API
            source = urllib.request.urlopen(api_url).read()
            
            # Convert JSON data to a Python dictionary
            list_of_data = json.loads(source)

            # Extract the necessary data
            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
                "temp": str(list_of_data['main']['temp']) + 'k',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
            }
        except Exception as e:
            # Handle potential errors (e.g., invalid city name, network issues)
            data = {"error": "Could not retrieve data. Please check the city name or try again later."}
            print(f"Error: {e}")
    else:
        data = {}
    
    # Render the template with the data
    return render(request, 'weather/index.html', data)
