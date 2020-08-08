import pandas as pd


data = pd.read_csv("Files/Volcanoes.txt")


lat = list(data["LAT"])
lon = list(data["LON"])
elev =list(data["ELEV"])


#print(data["ELEV"].max())
#print(data)