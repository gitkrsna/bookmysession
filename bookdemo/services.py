import os
import requests
import datetime

course_name = []
url = 'https://script.googleusercontent.com/macros/echo?user_content_key=K4BWRv-vTIFptxl3UD_I_3TK1O5LLaprpHxvNDk-TofDr7S1qFxdEkerD8BSL5C1QqsviUdwn3aUbHm1o6UmjHLyv9Q3kedUm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnC09Nb0QZ6ca_LU0vmo6mSiQ7SyFG3CgdL9-1Vgcha-TAYaAGhh-9xNG-9rMNEZHQRElvdDletx0&lib=MlJcTt87ug5f_XmzO-tnIbN3yFe7Nfhi6'
r = requests.get(url)
data = r.json()

course_name = []
course_id = []

date_slot = []
time_slot = []
dates_slot = []

length_of_total_data = len(data)

for j in range(length_of_total_data):    
	courses, id = data[j]['course_name'], data[j]['course_id']
    #course_name.append(courses)
    #course_id.append(id)
    
	for i in range(len(data[j]['slots'])):

		x=data[j]['slots'][i]['slot']
        
		dates=datetime.datetime.fromtimestamp(int(x[0:10])).strftime('%Y-%m-%d %H:%M') ,course_id.append(id),course_name.append(courses), 
        # date_slot.append(dates)
        
		times =datetime.datetime.fromtimestamp(int(x[0:10])).strftime('%H:%M') ,date_slot.append(dates), time_slot.append(date_slot[i][0][11:])
        # time_slot.append(times)
        

for i in range(len(course_name)):
    dates_slot.append(date_slot[i][0][0:10])

final_data=[]        

for i in range(len(course_name)):
    final_data.append(str(course_name[i])+" "+str(dates_slot[i]) +" "+str(time_slot[i]))


  
  

	


