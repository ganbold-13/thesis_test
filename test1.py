#!/usr/bin/env python3

from requests_tor import *
from bs4 import BeautifulSoup
import pandas as pd

requests = RequestsTor(tor_ports=(9050,), tor_cport=9051)

# url = 'http://ransomwr3tsydeii4q43vazm7wofla5ujdajquitomtd47cxjtfgwyyd.onion/'
url = 'http://breachedu76kdyavc6szj6ppbplfqoz3pgrk3zw57my4vybgblpfeayd.onion/Forum-Databases'
_cookies = {'dcap':'W+zM7Kz867fE7DbUyxr+Mir+JAh+bECcBGRTuKUBkGHKjc3ZTuhkCQPjKmQ97ud6nXbqYNnyapAPf8D1iJbuM1Ih1W1x8hwpdz5dBEJReKxepN7CFNSOAfOxsSEg5eCdJ3vfKmzKKw79aDFqVdvbii399ZdBbuafoSIboHO/Ats=',
            'loginattempts':'1',
            'mybb[announcements]':'0',
            'mybb[lastactive]':'1714417984',
            'mybb[lastvisit]':'1714416976',
            'mybbuser':'195220_3jifzZZHXCuHYAFKG3ABSMNeRsNKCjNKb9fBeF8w2xGMIdDmtZ',
            'sid':'ffcf4109551d02447c917d3a360c4bf4'}

r = requests.get(url, cookies=_cookies)
soup = BeautifulSoup(r.text, 'html')

dbs = [i.text for i in soup.find_all('span', class_='subject_new')]

df = pd.DataFrame(columns=['Titles'])
for i in dbs:
    length = len(df)
    df.loc[length] = [i]
print(df)

#print('\n'.join(dbs))
