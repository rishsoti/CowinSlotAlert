# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:54:03 2021

@author: rishabh.soti
"""
import time
import numpy as np
import pandas as pd
import smtplib
from cowin_api import CoWinAPI

date = '09-05-2021'
min_age_limit = 18 
empty_array = np.empty((0,6), int)

cowin = CoWinAPI()
districts = cowin.get_districts(34)
for i in districts['districts']:
    available_centers = cowin.get_availability_by_district(i['district_id'], date, min_age_limit)
    for i in available_centers['centers']:
       for x in i['sessions']:
           if int(x['available_capacity'])>0 :
             empty_array = np.append(empty_array, np.array([[str(i['name']),str(i['address']), str(x['available_capacity']), str(x['vaccine']), str(x['date']), str(x['slots'])]]), axis=0)
       
headers = ['Name','Address', 'Avilability', 'Vaccine', 'Date','Slots']
df = pd.DataFrame(empty_array, columns=headers)
html = df.to_html()
         
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
  
# start TLS for security
s.starttls()
  
# Authentication
s.login("no.reply.alert0@gmail.com", "noreplyuser")
  
# message to be sent
message = """From:  <from@fromdomain.com>
To:  <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: Alert!! Vaccine Slot Avilable

<h2><b> Book Your Appointment!!</b></h2>
<h2> </h2>
<h3> In any of the given hospital from Cowin App</h2>
<h3> -------------------------------------------</h2>
""" +html
time.sleep(2.4)
# sending the mail
s.sendmail("no.reply.alert0@gmail.com", "rishabhsoti16@gmail.com", message)
time.sleep(2.4)
# terminating the session
s.quit()
