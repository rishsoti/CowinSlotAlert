# CowinSlotAlert


Tracker to check the covid vaccine slot availability in India and send email through Smtp Service.


## Requirements

Mentioned in requirments.txt

## How to use?

1-Just go to  CowinScheduler.py update the state code for the state in which you want to search (you can get all state codes in StatesCodeList.txt file).

2- Update date , mail id , password and receiver mail id as per your details

3- Go on this link https://www.google.com/settings/security/lesssecureapps and provide the permission.

4-Run the python file or schedule them on task scheduler .

5- Enjoy!!!


## Notes:

1- You can also get data by pincode just remove state forloop and update

```Python
available_centers = cowin.get_availability_by_district(district_id, date, min_age_limit)

```
to

```Python
available_centers = cowin.get_availability_by_pincode(pin_code, date, min_age_limit)
```

2- You can also remove if condition of 18+ to get details for 45+ age group slots.

3- Please try not to spam the CoWin servers and try to keep a timeout between subsequent requests as sometime it  may  return a 401 Unauthorized response if you are not polling at a fixed interval gap

## Contributions

Contributions are always welcome!

