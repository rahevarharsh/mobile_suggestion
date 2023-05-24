import streamlit as st
import pandas as pd
import pipe

df = pd.read_csv('./Data/mobile_price_data.csv')

st.title('Mobile Phone suggestion')

l_price = st.text_input('Enter Low Price :', )
# st.write('Your Price : ', l_price)
h_price = st.text_input('Enter High Price :', )
# st.write('Your Price : ', h_price)

ram = st.selectbox(
    'Select RAM : ',
    ('1 GB', '2 GB', '3 GB', '4 GB', '6 GB', '8 GB', '12 GB'))
# st.write('You selected:', ram)

memory = st.selectbox(
    'Select ROM : ',
    ('8 GB', '16 GB', '32 GB', '64 GB', '128 GB', '256 GB', '512 GB'))
# st.write('You selected:', memory)

battery = st.selectbox(
    'Select Battery : ',
    ('2000 mAh', '2600 mAh', '2730 mAh', '3000 mAh', '3010 mAh',
     '3050 mAh', '3075 mAh', '3080 mAh', '3180 mAh', '3200 mAh',
     '3225 mAh', '3260 mAh', '3360 mAh', '3400 mAh', '3500 mAh',
     '3600 mAh', '3700 mAh', '3730 mAh', '4000 mAh', '4020 mAh',
     '4025 mAh', '4030 mAh', '4035 mAh', '4065 mAh', '4100 mAh',
     '4200 mAh', '4230 mAh', '4300 mAh', '4350 mAh', '4500 mAh',
     '4780 mAh', '5000 mAh', '5020 mAh', '6000 mAh'))
# st.write('You selected:', battery)

primary_camera = st.selectbox(
    'Select Primary Camera : ',
    ('108MP Rear Camera', '12MP + 13MP', '12MP + 20MP', '12MP + 2MP',
     '12MP + 2MP + 2MP', '12MP + 5MP', '12MP + 5MP + 8MP',
     '12MP + 8MP + 2MP + 2MP', '12MP Rear Camera',
     '13 MP + 2 MP + 2 MP + Low Light Sensor', '13MP + 2MP',
     '13MP + 2MP + 8MP',
     '13MP + 2MP Depth Sensor + 8MP Wide Angle sensor',
     '13MP + 8MP + 2MP', '13MP + 8MP + 2MP + 2MP', '13MP Rear Camera',
     '16MP + 20MP', '16MP + 2MP', '16MP + 2MP + 8MP',
     '16MP + 2MP + Low Light Sensor', '16MP + 5MP',
     '16MP + 5MP + 2MP + Low Light Sensor', '16MP + 8MP + 2MP',
     '16MP Rear Camera', '20MP + 12MP',
     '48 MP + 2 MP + 2 MP + Low Light Sensor',
     '48 Million Quad Pixel Sensor (12 Million Effective Pixel) + 8MP + 5MP, AI Triple Rear Camera',
     '48MP + 12MP + 5MP', '48MP + 13MP + 8MP',
     '48MP + 13MP + 8MP + 2MP', '48MP + 2MP + Low Light Sensor',
     '48MP + 5MP', '48MP + 5MP + 8MP', '48MP + 8MP',
     '48MP + 8MP + 13MP + 2MP', '48MP + 8MP + 2MP',
     '48MP + 8MP + 2MP + 2MP', '48MP + 8MP + 2MP + 2MP Quad Camera',
     '48MP + 8MP + 5MP', '48MP + 8MP + 5MP + 2MP', '5MP Rear Camera',
     '64MP + 12MP + 8MP + 2MP', '64MP + 13MP + 8MP + 2MP',
     '64MP + 8MP + 2MP + 2MP', '64MP + 8MP + 2MP + 2MP Quad Camera',
     '64MP + 8MP + 5MP + 2MP', '64MP + 8MP + 5MP + 5MP',
     '64MP + 8MP + 8MP + 2MP', '8MP Rear Camera'))
# st.write('You selected:', primary_camera)

front_camera = st.selectbox(
    'Select Front Camera : ',
    ('13MP + 2MP Dual Front Camera', '13MP Front Camera',
     '16MP + 8MP Dual Front Camera', '16MP Front Camera',
     '20MP + 2MP Dual Front Camera', '20MP Front Camera',
     '24MP Front Camera', '25MP Front Camera', '2MP Front Camera',
     '32MP + 8MP Dual Front Camera', '32MP Front Camera',
     '44MP + 2MP Dual Front Camera', '5MP Front Camera',
     '8MP Dual Front Camera', '8MP Front Camera'))
# st.write('You selected:', front_camera)

# l_price,h_price,ram,memory,battery,primary_camera,front_camera

if st.button('Get'):
    st.write(pipe.filter(l_price,h_price,ram,memory,battery,primary_camera,front_camera).loc[:,['phone_lable','mobile_price','ram','int_memory']].reset_index(drop=True))
# ['phone_lable','mobile_price']