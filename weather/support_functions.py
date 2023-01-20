from weather.models import City_m


def DMS_to_decimal(dms_coordinates):
    degrees = int(dms_coordinates.split('°')[0])
    minutes = int(dms_coordinates.split('°')[1].split("′")[0])
    try:
        seconds = int(dms_coordinates.split('°')[1].split("′")[1][:2])
    except:
        seconds = 0.0
    decimal = degrees + minutes/60 + seconds/3600
    try:
        if dms_coordinates[-1] == "S":
            decimal = -decimal
    except:
        pass
    try:
        if dms_coordinates[-1] == "W":
            decimal = -decimal
    except:
        pass
    return decimal

def get_lat_lon(city_name):
    import requests
    from bs4 import BeautifulSoup
    try:
         city = City_m.objects.get(name=city_name)
         lat = city.latitude
         lon = city.longitude
         wiki_link = ""
    except:
         url = "https://en.wikipedia.org/wiki/"
         url += city_name.replace(" ","_")
         wiki_link = url
    try:
         text = requests.get(url).text
         soup = BeautifulSoup(text)
         lat = soup.find('span', class_="latitude").get_text()
         lon = soup.find('span', class_="longitude").get_text()
         lat = DMS_to_decimal(lat)
         lon = DMS_to_decimal(lon)
    except:
         lat = 0.0
         lon = 0.0
    return lat,lon,wiki_link

def add_markers(m,visiting_cities):
    import folium
    lat_lon_list = list()
    for city_name in visiting_cities:
         lat,lon,wiki_link = get_lat_lon(city_name)
         print(city_name,lat,lon,wiki_link)
         if lat != 0.0 and lon != 0.0 and wiki_link != "":
             icon = folium.Icon(color="blue",prefix="fa",icon="plane")
             popup = "<a href="
             popup += wiki_link
             popup += ">" + city_name+ "</a>"
             marker = folium.Marker((lat,lon),icon=icon,popup=popup)
             marker.add_to(m)
             lat_lon_list.append([lat,lon])
 #Add line. First rearrange lat lons by longitude
    lat_lon_list.sort(key=lambda x: x[1])
    line_string = list()
    for i in range(len(lat_lon_list)-1):
        line_string.append([lat_lon_list[i],lat_lon_list[i+1]])
    line = folium.PolyLine(line_string,color="red",weight=5)
    line.add_
    return m