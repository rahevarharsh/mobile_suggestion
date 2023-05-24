import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import FunctionTransformer,LabelEncoder
import re

df1=pd.read_csv('./Data/mobile_price_data.csv')
df1.drop_duplicates(inplace=True)

df = df1.loc[:,['mobile_price','ram','int_memory','p_cam','f_cam','battery_power']]

def convert(df):
    df['mobile_price']=(df['mobile_price'].str.replace(',','').str.replace('₹',''))
    df['mobile_price']=df['mobile_price'].apply(lambda x:int(x))
    
    def number_convert(k):
        return re.findall(r'\d+', k)[0]
    
    df['p_cam']=df['p_cam'].apply(number_convert)
    df['f_cam'] = df['f_cam'].apply(number_convert)

    df['int_memory']=df['int_memory'].str.replace('GB','')
    df['ram']=df['ram'].str.replace('GB','')
    df['battery_power']=df['battery_power'].str.replace('mAh','')
    
    df['ram'] = df['ram'].apply(lambda x:int(x))
    df['int_memory'] = df['int_memory'].apply(lambda x:int(x))
    df['p_cam'] = df['p_cam'].apply(lambda x:int(x))
    df['f_cam'] = df['f_cam'].apply(lambda x:int(x))
    df['battery_power'] = df['battery_power'].apply(lambda x:int(x))
  
    return df.loc[:,['mobile_price','ram','int_memory','p_cam','f_cam','battery_power']]

ft = FunctionTransformer(convert)

pipe = Pipeline([('convert',ft),('DecisionTreeClassifier',DecisionTreeClassifier())])

y = df1['mobile_name']
lb = LabelEncoder()
y=lb.fit_transform(y)
pipe.fit(df.copy(),y)

def predict(row):
    return pipe.predict(row)


def number_convert1(k):
    return re.findall(r'\d+', k)[0]
    

def filter(low,high,ram,memory,battery,primary_camera,front_camera):
    temp = df.copy()
    pipe.fit(temp,y);
    temp['phone_lable'] =lb.inverse_transform( y)
    temp = temp[(temp['mobile_price']>int(low))&(temp['mobile_price']<int(high))].sort_values('mobile_price',ascending=False);
    if (len(temp)<6)&(len(temp)!=0):
        return temp
    battery = int(battery.replace('mAh',''))
    primary_camera = int(number_convert1(primary_camera))
    front_camera = int(number_convert1(front_camera))
    temp_battery_power=temp[(temp['battery_power']==(battery))]
    if (len(temp)<7)&(len(temp)!=0):
        return temp
    ram = int(ram.replace('GB',''))
    memory = int(memory.replace('GB',''))
    temp_ram = temp_battery_power[temp_battery_power['ram']==ram]
    if len(temp_ram)==0:
        return temp_battery_power
    temp_memory = temp_ram[temp_ram['int_memory']==memory]
    if (len(temp_memory)==0):
        return temp_ram
    temp_primary_camera=temp_memory[temp_memory['p_cam']==primary_camera]
    if (len(temp_primary_camera)==0):
        return temp_memory
    temp_front_camera=temp_primary_camera[temp_primary_camera['f_cam']==front_camera]
    if (len(temp_front_camera)==0):
        return temp_primary_camera
    return temp_front_camera 