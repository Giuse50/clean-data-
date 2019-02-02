import pandas as pd


marriage= pd.read_excel('state-marriage-rates-90-95-99-17.xlsx',
                        skiprows=4,
                        header=[0,1],
                        skipfooter=7,
                        na_values='NA',
                        usecols=2,
                        index_col=[0,1])

marriage = marriage.stack()

print(marriage)