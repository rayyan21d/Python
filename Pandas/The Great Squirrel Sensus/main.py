import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#Get all grey squirrels
grey_squirrels = data[ data["Primary Fur Color"] == "Gray" ]
grey_squirrels_count = len(grey_squirrels)  

#Get all red squirrels
red_squirrels = data[ data["Primary Fur Color"] == "Cinnamon" ]
red_squirrels_count = len(red_squirrels)

#Get all black squirrels
black_squirrels = data[ data["Primary Fur Color"] == "Black" ]
black_squirrels_count = len(black_squirrels)

#Creating a new dictionary
dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

dataframe = pandas.DataFrame(dict)
dataframe.to_csv("squirrel_count.csv")