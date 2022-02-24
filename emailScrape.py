import re
import json
import pandas as pd

with open('websiteData.txt','r',encoding='UTF-8') as file:
    emails =  re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", file.read())
    type = []
    df = pd.DataFrame(emails, columns = ['Emails'])
    for email in df['Emails']:
        print(email)
        first_part = email.split('@')
        if '.' in first_part[0]:
            type.append('Human')
        
        elif len(first_part[0]) < 8:
            type.append('Non-Human')
        else:
            type.append('Non-Human')
    
    
        
    df['Email-Type'] = type
    to_json = []
    for email,type in zip(df['Emails'],df['Email-Type']):
        to_json.append({email:{'occurrence':int(df['Emails'].value_counts()[email]),'EmailType':str(type)}})
    with open('result.json', 'w') as json_file:
         json.dump(to_json, json_file)
    
    

        
