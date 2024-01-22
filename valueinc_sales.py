# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 18:23:01 2023

@author: amask
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <--- format of read_csv
data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv',sep=';')

#summary of the data
data.info()


#working with calculations

#defining varialbes

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#mathematical operations on Tableau

ProfitPerItem = 21.11 - 11.73

ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = CostPerItem * NumberOfItemsPurchased
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased

#CostPerTransaction Column Calculation

#CostPerTransaction = CostPerItem * NumberOfItemsPurchased
# variable = dataframe['column_name']
CostPerItem = data['CostPerItem']

NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#Adding a new column to dataframe

data['CostPerTransaction'] = CostPerTransaction

#Sales per transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit per transaction
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup per transaction = (Sales - Cost) / Cost
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']
data['Markup'] = (data['ProfitPerTransaction'])/data['CostPerTransaction']

#Rounding markup up 2

roundmarkup = round(data['Markup'], 2)

data['Markup'] = roundmarkup

#combining data fields

my_name = 'Anthyun' + 'Mask'
my_date = 'Day'+'-'+'Month'+'-'+'Year'

#Checking columns data type
print(data['Day'].dtype)

#Change column type

day = data['Day'].astype(str)
print(day.dtype)

year = data['Year'].astype(str)
print(year.dtype)


my_date = day + '-' + data['Month'] + '-' + year

data['Date'] = my_date

#Using iloc to view specific column/rows

data.iloc[0] #views the row where index = 0
data.iloc[0:3] #view 1st 3 rows
data.iloc[-5:] #view last 5 rows

data.head(5) #brings in 1st 5 rows

data.iloc[:,2] #brings in all rows, 2nd column
data.iloc[4,2] #brings in 4th row, 2nd column

#using split to split the client keyword fields
#new_var - column.str.split('sep' , expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand = True)

#create new columns for the split columns in client keyword

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using the replace function to replace brackets

data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']', '')

#using the lower function to change string to lower case

data['ItemDescription'] = data['ItemDescription'].str.lower()

#bringing new dataset

seasons = pd.read_csv('value_inc_seasons.csv',sep=';')

#merging files: merge.df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#using drop columns
#df = df.drop('columnname', axis = 1)

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Month','Year'], axis = 1)


#Export into csv

data.to_csv('ValueIncCleaned.csv', index = False)


































