import streamlit as st
import time
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler



#______________________________________________CACHE ELEMENTS FUNCTIONS



@st.cache_resource
def cargar_imagen():    
    return "banner_01.jpg"

@st.cache_resource
def load_ml():    
    classifier = joblib.load('modelo_gama.pkl')  # High/Low price
    return  classifier

@st.cache_resource
def load_ml_r():    
    tree = joblib.load('price_model.pkl')  # Price stimator
    return  tree

@st.cache_resource
def load_sc():    
    sc = joblib.load('sc_gama.pkl')
    return  sc

#Load models
classifier = load_ml()
sc = load_sc()

tree = load_ml_r()

#______________________________________________VARIABLES

ruta_img = cargar_imagen()


wheelbase = 87     # Valores entre 87 y 115
carlength = 141       # Valores entre 141 y 202
carwidth = 47        # Valores entre 47 y 59
carheight = 60       # Valores entre 60 y 72
curbweight = 1488      # Valores entre 1488 y 4066
enginesize = 61      # Valores entre 61 y 326
boreratio = 2.5       # Valores entre 2.5 y 3.9
compressionratio = 7        # Valores entre 7 y 23
horsepower = 48      # Valores entre 48 y 288
citympg = 13         # Valores entre 13 y 49
highwaympg =17      # Valores entre 17 y 53
price_log = 0 
enginesize_log = 0      
curbweight_log = 0     
fueltype_diesel = 0 #
fueltype_gas = 0    #
aspiration_std = 0      #
aspiration_turbo = 0    
carbody_convertible = 0  #
carbody_hatchback = 0   
carbody_sedan = 0   
drivewheel_fwd = 0  
drivewheel_rwd = 0  
enginelocation_front = 0    
enginelocation_rear = 0     
enginetype_dohc = 0         #
enginetype_l = 0             
enginetype_ohc = 0           
enginetype_ohcf = 0         
enginetype_ohcv = 0         
cylindernumber_eight = 0    #
cylindernumber_five = 0     
cylindernumber_four = 0     
cylindernumber_six = 0      
fuelsystem_1bbl = 0         #
fuelsystem_2bbl = 0         
fuelsystem_idi = 0          
fuelsystem_mpfi = 0         
price = 5118   #Low price



v_gama = [wheelbase, carlength, carwidth, carheight, curbweight, enginesize, boreratio, compressionratio,
          horsepower, citympg, highwaympg, price_log, enginesize_log, curbweight_log, fueltype_diesel, 
          fueltype_gas, aspiration_std, aspiration_turbo, carbody_convertible, carbody_hatchback, 
          carbody_sedan, drivewheel_fwd, drivewheel_rwd, enginelocation_front, enginelocation_rear, 
          enginetype_dohc, enginetype_l, enginetype_ohc, enginetype_ohcf, enginetype_ohcv, cylindernumber_eight, 
          cylindernumber_five, cylindernumber_four, cylindernumber_six, fuelsystem_1bbl, fuelsystem_2bbl, 
          fuelsystem_idi, fuelsystem_mpfi,price]

v_price = [wheelbase, carlength, carwidth, carheight, curbweight,
       enginesize, boreratio, compressionratio, horsepower, citympg,
       highwaympg, enginesize_log, curbweight_log, fueltype_diesel,
       fueltype_gas, aspiration_std, aspiration_turbo,
       carbody_convertible, carbody_hatchback, carbody_sedan,
       drivewheel_fwd, drivewheel_rwd, enginelocation_front,
       enginelocation_rear, enginetype_dohc, enginetype_l,
       enginetype_ohc, enginetype_ohcf, enginetype_ohcv,
       cylindernumber_eight, cylindernumber_five, cylindernumber_four,
       cylindernumber_six, fuelsystem_1bbl, fuelsystem_2bbl,
       fuelsystem_idi, fuelsystem_mpfi]

#________________________________________________REGISTER FORM 
with st.form('valueCheck',  clear_on_submit=True):
    
    st.image(ruta_img)   
    st.divider()#__________________________________________

    st.subheader('Physical characteristics of the car:')
    
    with st.expander('Sellect:'):
        n1, n2, n3, n4 = st.columns([1,2,1,2], gap='medium')
        with n1:
            st.subheader('')
            st.write('Wheelbase')
        with n2:
            wheelbase = st.slider('Wheelbase', 87,115,87, step=1, label_visibility='hidden')
            
        with n3:
            st.subheader('')
            st.write('Carwidth')
        with n4:
            carwidth = st.slider('carwidth', 1488,4086,1488, step=1, label_visibility='hidden')    
            
            
        n5, n6, n7, n8 = st.columns([1,2,1,2,], gap='medium')
        
        with n5:
            st.subheader('')
            st.write('Carlength')
            st.subheader('')
            st.subheader('')
            st.write('Carhight')
        with n6:
            carlength = st.slider('Carlength', 141,202,141, step=1, label_visibility='hidden')
            carheight = st.slider('Carhight', 60,72,60, step=1, label_visibility='hidden')
        with n7:
            st.subheader('')
            st.write('Curbweigh')
        with n8:
            curbweigh = st.slider('Curbweigh', 60,72,60, step=1, label_visibility='hidden')
        
    st.divider()#__________________________________________
        
    
    st.subheader('Engine specifications')        # Single sellection
    with st.expander('Sellect:'):    
        u1, u2, u3, u4 = st.columns([1,2,1,2], gap='medium')
        with u1:
            st.subheader('')
            st.write('Enginesize')
        with u2:
            enginesize = st.slider('Enginesize', 61,326,61, step=1, label_visibility='hidden')
            
        with u3:
            st.subheader('')
            st.write('Boreratio')
        with u4:
            boreratio = st.slider('Boreratio', 1488,4086,1488, step=1, label_visibility='hidden')    
            
            
        u5, u6, u7, u8 = st.columns([1,2,1,2], gap='medium')
        
        with u5:
            st.subheader('')
            st.write('Compressionratio')
            
        with u6:
            compressionratio = st.slider('Compressionratio', 141,202,141, step=1, label_visibility='hidden')
            
        with u7:
            st.subheader('')
            st.write('Horsepower')
        with u8:
            horsepower = st.slider('Horsepower', 60,72,60, step=1, label_visibility='hidden')
        
    st.divider()#__________________________________________
    
    st.subheader('Additional specifications:')
    with st.expander('Sellect:'): 
        u9, u10, u11, u12 = st.columns([1,1,1,1], gap='medium')
        
        with u9:
            st.subheader('')
            st.write('citympg')
            
        with u10:
            citympg = st.slider('Citympg', 13,49,13, step=1, label_visibility='hidden')
            
        with u11:
            st.subheader('')
            st.write('Highwaympg')
        with u12:
            highwaympg = st.slider('Highwaympg', 17,53,17, step=1, label_visibility='hidden')
        
        st.divider()#__________________________________________

        # with u13:
        e1, e2 = st.columns([1,1], gap='medium')
        
        with e1:
            fuel_type =st.radio('', ['fueltype_diesel', 'fueltype_gas'],
                            index=None, horizontal=False)  
            st.divider()#__________________________________________
            aspiration =st.radio('', ['aspiration_std', 'aspiration_turbo'],
                            index=None, horizontal=False)  
            
            st.divider()#__________________________________________        
            enginelocation =st.radio('', ['enginelocation_front', 'enginelocation_rear'],
                            index=None, horizontal=False)
            st.divider()#__________________________________________        
            cylindernumber =st.radio('', ['cylindernumber_eight', 'cylindernumber_five',
                                        'cylindernumber_four', 'cylindernumber_six'],
                            index=None, horizontal=False)
            
            
            

        with e2:
            carbody =st.radio('', ['carbody_convertible', 'carbody_hatchback', 'carbody_sedan'],
                            index=None, horizontal=False) 
            st.divider()#__________________________________________
            
            drivenwheel =st.radio('', ['drivewheel_fwd', 'drivewheel_rwd'],
                            index=None, horizontal=False)
            
            st.divider()#__________________________________________        
            enginetype =st.radio('', ['enginetype_dohc', 'enginetype_l', 'enginetype_ohc', 
                                    'enginetype_ohcf', 'enginetype_ohcv'],
                            index=None, horizontal=False)
            
            st.divider()#__________________________________________        
            fuelsystem =st.radio('', ['fuelsystem_1bbl', 'fuelsystem_2bbl', 'fuelsystem_idi', 
                                    'fuelsystem_mpfi'],
                            index=None, horizontal=False)



    st.divider()#__________________________________________
    s_button = st.form_submit_button("Calculates value")
    
    
    
    if s_button:
        
        if fuel_type == 'fueltype_diesel':  ### Fuel Type
            fueltype_diesel = 1
        
        elif fuel_type == 'fueltype_gas':
            fueltype_gas = 1
        
        if aspiration == 'aspiration_std':
            aspiration_std = 1
            
        elif aspiration == 'aspiration_turbo':
            aspiration_turbo = 1
        
        if enginelocation == 'enginelocation_front':
            enginelocation_front = 1
            
        elif enginelocation == 'enginelocation_rear':
            enginelocation_rear = 1
        
        if cylindernumber == 'cylindernumber_eight':
            cylindernumber_eight = 1            
        elif cylindernumber == 'cylindernumber_five':
            cylindernumber_five = 1
        elif cylindernumber == 'cylindernumber_four':
            cylindernumber_four = 1
        elif cylindernumber == 'cylindernumber_six':
            cylindernumber_four = 1
            
        if carbody == 'carbody_convertible':
            carbody_convertible = 1
        elif carbody == 'carbody_hatchback':
            carbody_hatchback = 1
        elif carbody == 'carbody_sedan':
            carbody_sedan = 1
        
        if drivenwheel == 'drivewheel_fwd':
            drivewheel_fwd = 1
        elif drivenwheel == 'drivewheel_rwd':
            drivewheel_rwd = 1
        
        if enginetype == 'enginetype_dohc':
            enginetype_dohc = 1 
        elif enginetype == 'enginetype_l':
            enginetype_l = 1
        elif enginetype == 'enginetype_ohc':
            enginetype_ohc = 1
        elif enginetype == 'enginetype_ohcf':
            enginetype_ohcf = 1   
        elif enginetype == 'enginetype_ohcv':
            enginetype_ohcv = 1   
        
        if fuelsystem == 'fuelsystem_1bbl':
            fuelsystem_1bbl = 1
        elif fuelsystem == 'fuelsystem_2bbl':
            fuelsystem_2bbl = 1 
        elif fuelsystem == 'fuelsystem_idi':
            fuelsystem_idi = 1    
        elif fuelsystem == 'fuelsystem_mpfi':
            fuelsystem_mpfi = 1   
        
        # Logaritmic transformation
        
        enginesize_log = np.log(enginesize)
        curbweight_log = np.log(curbweight)
        
        w_pred = tree.predict([v_price])
        price = int(w_pred[0])
        st.subheader(f'The price of the car will be {price}')
        g_pred = classifier.predict(sc.transform([v_gama]))
        g_value = int(g_pred[0])
        
        st.write('')
        if g_pred == 0:
            st.subheader('Economic class type car')
        else:
            st.subheader('High class type car')
        
        
