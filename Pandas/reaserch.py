#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd

people= {
    "first" :["Ania", "Marysia", "Ola"],  
    "last" :["Osten", "Marck", "Sir"],
    "email": ["@gmail", "@pl", "@.com"]}
df = pd.DataFrame(people)
df.append({'first':'Kaja', 'last': 'Mokosz', 'email':'@'}, ignore_index =True)
print(df)