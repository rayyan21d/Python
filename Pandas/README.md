# Data Processing CSV and Pandas

Python is widely used for data processing and analysis. It has a lot of built in support for data. One of the common type of data is CSV data. This is used to represent tabular data. Python has a built in module called csv to process csv data. It also has a built in module called pandas to process csv data. Pandas is a very powerful module for data processing. It is very fast and efficient. It is also very easy to use. It is very popular among data scientists. It is also used in machine learning. In this article we will see how to use pandas to process csv data.


## Reading CSV Data

`with open(data.csv) as file:
    data = file.readline()
print(data) `
This returns a list, but it also has a lot of extra characters. We can use the strip() function to remove the extra characters. We can also use the split() function to split the string into a list of values. We can use the next() function to skip the first row which is the header row.


`import csv
with open(data.csv) as file:
data = csv.reader(file)
`
Without the csv library, the data we get using readline() has all sorts of extra characters. The csv library helps us to read the data in a more structured way. We can use the csv.reader() function to read the data. This function returns an object which can be looped through. Each row is a list of values. We can use the next() function to skip the first row which is the header row.

With the use of Pandas this becomes a piece of cake

'import pandas as pd
data = pd.read_csv(data.csv)'

This creates a dataframe and assigns it to the variable data.

## What is a Dataframe?
Pandas has two important objects that make it powerful. Series and dataframes. A series is a one dimensional array. A dataframe is a two dimensional array. A dataframe is a collection of series. A dataframe is like a table. It has rows and columns. Each column is a series. A dataframe can be created from a dictionary. The keys of the dictionary become the column names. The values of the dictionary become the values of the series. The keys of the dictionary become the column names. 
## Writing CSV Data

