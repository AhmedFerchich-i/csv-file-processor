from fastapi import FastAPI
import os
from dotenv import load_dotenv
import pandas
load_dotenv()
app=FastAPI()

@app.get('/stats/{file_name}/')
def get_file_stats(file_name:str):
    files_location=os.getenv('FILES_LOCATION')
    file_path=os.path.join(files_location,file_name)
    
    df=pandas.read_csv(file_path)
    headers=df.columns.to_list()
    print(headers)
    response_dict={}
    entries_number=df.shape[0]
    response_dict['total_entries']=entries_number
    for h in headers:
        try:
         response_dict[h]={'min':float(df[h].min()),'max':float(df[h].max()),'avg':float(df[h].mean())}
        except:
           response_dict[h]='non numeric column'
    return(response_dict)

