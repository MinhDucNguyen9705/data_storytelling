import pandas as pd 
import numpy as np 

customer = pd.read_csv('customer.csv')
ticket = pd.read_csv('ticket.csv')
film = pd.read_csv('film.csv')

print(customer.columns)
print(ticket.columns)
print(film.columns)

#hello 