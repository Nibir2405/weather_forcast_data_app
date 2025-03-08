import requests

API_Key = "44555c9be8695963a8ccc6aea022368f"



def get_data(place, forcast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_Key}"
    respond = requests.get(url)
    data = respond.json()
    filtered_data = data["list"]
    nr_value = 8*forcast_days
    filtered_data = filtered_data[0:nr_value]
    
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forcast_days=3))