import pandas as pd 
import numpy as np 

customer = pd.read_csv('data_cleaning/customer.csv')
ticket = pd.read_csv('data_cleaning/ticket.csv')
film = pd.read_csv('data_cleaning/film.csv')

print(customer.head())
print(ticket.head())
print(film.head())

#hello 