import pandas as pd

#print("Hello World")

#Ejercicio 3
'''data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame)'''

#Ejercicio 4
'''data = pd.Series([23,45,7,34,6,63,36,78,54,34])
print(data)'''

#Ejercicio 4.1
'''fechas = pd.date_range(start='2021-05-01',end='2021-05-12')
print(fechas)'''

#Ejercicio 4.2
'''my_series = pd.Series([2,4,6,8,10])
mitad = my_series.apply(lambda x:x/2)
print(mitad)'''

#Ejercicio 5
'''data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data, columns=['Nombre','Edad'])
print(df)'''
'''data = [['Toyota','Corolla','Blue'],['Ford','K','Yellow'],['Porsche','Cayenne','White']]
df = pd.DataFrame(data, columns=['Brand','Model','Color'])
print(df)'''

#Ejercicio 5.1
'''data = [
    { 
        "brand": "Toyota", 
        "model": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "model": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porsche", 
        "model": "Cayenne",
        "color": "White"
    },
    {
        "brand": "Tesla", 
        "model": "Model S",
        "color": "Red"
    }
]
df = pd.DataFrame(data)
print(df)'''

#Ejercicio 5.2
'''data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame.iloc[133,6])'''

#Ejercicio 5.3
'''data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame.head(3))'''

#Ejercicio 5.4
'''data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame.tail(3))'''

#Ejercicio 5.5
'''data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame[['Name','Type 1']][0:10])'''

#Ejercicio 5.6
'''data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame.loc[data_frame['Attack']>80])'''

#Ejercicio 5.7
data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(len(data_frame.loc[data_frame['Legendary']==True]))
