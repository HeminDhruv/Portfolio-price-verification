# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 11:11:41 2022

@author: Hemin
"""

from pymysql import *
conn= connect (host='localhost', user='root', password = 'Snehmin@143', 
               db='ipv')
cur = conn.cursor()
u_i=input('enter stock name : ')
query='''select t1.stock_name, t1.qty, t1.desk_price, 
            t2.independent_price 
            from desk_data as t1
            inner join independent_prices as t2
            where t1.stock_name = t2.stock_name
            having stock_name="{}"'''.format(u_i)
cur.execute(query)


# cur.execute('select * from desk_data')

for i in cur:
    print (i)
    
conn.commit()
conn.close()


