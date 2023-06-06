# Install pandas first: pip install pandas
import pandas

data = pandas.read_csv('weather_data.csv')

#Converting to a list
temp_list = data['temp'].to_list()
print(temp_list)

#Average Temperature
print(data["temp"].mean())

#Converting to a dictionary
dict = data.to_dict()
print(dict)

