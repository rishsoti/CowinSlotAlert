# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:54:03 2021

@author: rishabh.soti
"""

import numpy as np
import pandas as pd
import smtplib
from cowin_api import CoWinAPI


pin_code = "243001"
date = '09-05-2021'  # Optional. Default value is today's date
min_age_limit = 45  # Optional. By default returns centers without filtering by min_age_limit 


empty_array = np.empty((0, 4), int)
cowin = CoWinAPI()
available_centers = cowin.get_availability_by_pincode(pin_code, date, min_age_limit)
print(available_centers)
for i in available_centers['centers']:
   for x in i['sessions']:
        empty_array = np.append(empty_array, np.array([[str(i['name']),str(i['address']), str(x['available_capacity']), str(x['vaccine']), str(x['date'])]]), axis=0)
       
headers = ['Name', 'Avilability', 'Vaccine', 'Date']
df = pd.DataFrame(empty_array, columns=headers)
html = df.to_html()
         
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
  
# start TLS for security
s.starttls()
  
# Authentication
s.login("no.reply.alert0@gmail.com", "FLYhigh91!")
  
# message to be sent
message = """From:  <from@fromdomain.com>
To:  <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: Alert!! Vaccine Slot Avilable




<h2><b> Book Your Appointment!!</b></h2>
<h2> </h2>
<h3> In any of the given hospital from Cowin App</h2>
""" +html
  
# sending the mail
s.sendmail("no.reply.alert0@gmail.com", "vs230135@gmail.com", message)
  
# terminating the session
s.quit()