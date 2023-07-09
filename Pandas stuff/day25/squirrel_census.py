import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_data = len(data[data["Primary Fur Color"] == "Gray"].X.to_list())
cinnamon_data = len(data[data["Primary Fur Color"] == "Cinnamon"].X.to_list())
black_data = len(data[data["Primary Fur Color"] == "Black"].X.to_list())
f = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_data, cinnamon_data, black_data]
}
fin = pd.DataFrame(data=f)

fin.to_csv("final.csv")
