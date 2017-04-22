import pandas as pd
from pandas import DataFrame, Series
import time


actor_names = pd.read_excel("~\S1234.xlsx")
n = actor_names.iterrows()
n_ls = []
for i in n:
    n_ls.append(i[1][0])
print n_ls


import urllib2, sys
from bs4 import BeautifulSoup
import re
my_list= []
k = 1
for names in n_ls:
    try:
        sites= 'http://www.metacritic.com/person/' + str(names)
        #sites= "http://www.metacritic.com/person/" + str(names) +'?filter-options=movies&sort_options=date&num_items=30'
        hdrs = {'User-Agent': 'Mozilla/5.0'}
        reqs = urllib2.Request(sites,headers=hdrs)
        pages = urllib2.urlopen(reqs)
        soups = BeautifulSoup(pages)
        real =soups.find_all("span","data textscore textscore_favorable") + soups.find_all("span","data textscore textscore_mixed")+soups.find_all("span","data textscore textscore_unfavorable")
        real = str(real)
        score =(re.sub(r'<.*?>', '', real)) 
        s =re.sub(r'\[', ' ', score)
        ss =re.sub(r'\]', ' ', s)
        q =[x.strip() for x in ss.split(',')]
        qq = [float(x) for x in q]
        qqq = max(qq)
        print '______________'
        print ' '
        print ' '
        print 'this is no.' + str(k) + ' actor from the list.'
        print ' '
        print ' '
        print str(names)  + ',' + str(qqq)
        my_list.append(str(names) + ',' + str(qqq))
        time.sleep(3)
        k += 1
    except:
        print 'error'
        print '--------------'
        continue
f = open("~\S3MS.csv", "w")
for item in my_list:
    f.write(str(item) + "\n")
f.close()


