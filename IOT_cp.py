from matplotlib.ft2font import LOAD_VERTICAL_LAYOUT
import numpy as np
import pandas as pd
import streamlit as st
import webbrowser
import pickle
from gsheetsdb import connect
from PIL import Image


#from pyexpat import model
#from re import A, X
#from turtle import ht
#from matplotlib.ft2font import LOAD_VERTICAL_LAYOUT
# import numpy as np
# import pandas as pd
# import streamlit as st
# import webbrowser
# import pickle
# #from collections.abc import Iterable
# # import scipy.stats as stats
# from gsheetsdb import connect


from PIL import Image

pickle_in = open("models/gassensor.pkl","rb")
model=pickle.load(pickle_in)

def predict_food(moisture,temp,gas):
    moisture = int(moisture)
    temp = int(temp)
    gas = int(gas)

    if (temp>30 and moisture>70 and gas>1500):
        x="Reduce the Temp to 30 ,moisture to 70 and gas to 5000"
    elif(temp<30 and moisture<70 and gas<1500):
        x="Increase the temp to 30 and moisture to 70 and gas to 1500" 
    elif(temp == 30 and moisture==70 and gas==1500):    
        x="Your food is safe" 
    
    return x

def predict_gas(gas_b):
   # float(gas_b)
    # zscore = float(gas_b) - float(2043.416465)
    # d =float(zscore) /4897.442071
    # str(d)	
   # arr=model.predict(np.array(d).reshape(-1,1))
    arr=model.predict(np.array(gas_b).reshape(-1,1))
    print(arr)
    #y = "This is gas DATA"
    return arr[0]
    #return y

def main():
    st.set_page_config(
    page_title="IOT BLOCKCHAIN",
    page_icon="✅",
    layout="wide",
    )
    #st.sidebar.markdown("# About 🎈")
    st.sidebar.title("Supply chain Monitoring")
    im = Image.open("images/download.jpg")
    st.sidebar.image(im)

    st.sidebar.title("About Us 🎈")
    st.sidebar.text("Vishwakarma Institue of Technology")
    st.sidebar.text("Electronics And Tellecommunications Engineering")
    st.sidebar.text("SY-ET-D-B2_Grp1")
    st.sidebar.title("Contributers🎉")
    st.sidebar.text("35) Sourjadip Pramanik")
    st.sidebar.text("50) Vaibhav Kadam")
    st.sidebar.text("53) Vijay Kumar Singh")
    st.sidebar.text("55) Vishal Gurudasani")
    #st.sidebar.text("56) Vishal Phonde")

    st.sidebar.title("Give us your review here")
    result = st.sidebar.text_input(label='Feedback',value='Write Here',max_chars=600)
    
    if len(result)>12:
        st.sidebar.success('Feedback sent Successfully')#'The output is {}'.format(result_g)'
        print(result)

    html_heading = """
    <div>
    
    <h1 style="color:white;text-align:center;font-family:georgia;"> REAL  TIME  FOOD  MONITORING  SYSTEM</h1>
    </div>
    """
    st.markdown(html_heading,unsafe_allow_html=True)
    #st.title("REAL TIME FOOD MONITORING SYSTEM")

    html_temp = """
    <div style="background-color:yellow;padding:10px">
    <h2 style="color:black;text-align:center;">FOOD CONDITION ANALYSIS</h2>
    </div>
    """
    st.write("")
    st.write("")
    st.write("")
    #image = Image.open('cp_main_img.jpg')

    

   

    col1, col2, col3 = st.columns([0.8,6,0.8])

    with col1:
        st.write("")

    with col2:
       # image = Image.open('IOT-info 1.webp')
        image = Image.open('images/1_aeaXMSzLw1tbsgSwUdZ1VA.jpeg')
        st.image(image, caption='Sensor Data on FOOD')

    with col3:
        st.write("")
    

    st.title("For geting Real Time Sensor Data")

    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #00cc00;color:white;font-size:40px;height:3em;width:50%;border-radius:10px 10px 10px 10px;position: center;
        left: 50%;
    }
    </style>""", unsafe_allow_html=True)

    if  st.button("THINGSPEAK"):

    #if st.button("THINGSpeak"):
        webbrowser.open('https://thingspeak.com/channels/1733229/private_show')  # Go to example.com

   
    st.header("Here, you can see the real time data of the food (BANANNA)")
    

    st.markdown(html_temp,unsafe_allow_html=True)
    st.header("Moisture")
    moisture = st.text_input(" ","Type Here")
    st.header("Temperature")
    temp = st.text_input("  ","Type Here")
    st.header("Gas")
    gas = st.text_input("   ","Type Here")
    # gas = st.text_input("Gas","Type Here")
    result=""

    st.header('The Output is')
    if st.button("Predict"):
        result=predict_food(moisture,temp,gas)

         
        st.success('{}'.format(result))#'The output is {}'.format(result_g)'
   
       # st.success("The food is save")
    st.write('')
    st.write('')
    st.write('')
    #header_t = st.title("Our DATASET FOR BANANNA")

    html_dataset = """
    <h2 style="color:white;text-align:center;">Our DATASET FOR BANANNA <a href = "https://github.com/Sourja99/Real-Time-Food-Assurance/blob/main/datasets/IOT_CP_Monitoring%20-%20Sheet1.csv">✅</a></h2>
    """
    st.markdown(html_dataset,unsafe_allow_html=True)

    st.write("")
    


    html_gas = """
    <div style="background-color:Red;padding:30px">
    <h2 style="color:white;text-align:center;">Dynamic Data Analysis </h2>
    </div>
    """
    
    # st.write("THE K-NN Analysis")
    # img = Image.open('images/download.png')
    # st.image(img,width=600,caption='10-NN Cluster Analysis on Air_Quality')

    st.markdown(html_gas,unsafe_allow_html=True)

    #conn = connect()
    
    st.title("Real Time Dataset")
     
    co1, co2, co3 = st.columns([0.8,6,0.8])


    with co1:
        st.write("")

    
    with co2:
       # image = Image.open('IOT-info 1.webp')
    #    st.cache(ttl=1)
    #    def run_query(query):
    #     rows = conn.execute(query, headers=1)
    #     rows = rows.fetchall()
    #     return rows
    #     # rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
    #     # return rows
    #    sheet_url = st.secrets["public_gsheets_url"]
    #    rows = run_query(f'SELECT * FROM "{sheet_url}"')

    #    df_gsheet = pd.DataFrame(rows)
    #    st.write(df_gsheet)


        # gsheet_url = "https://docs.google.com/spreadsheets/d/16ciPmGxI4p6_a1VdE1lwNNplm1OF0-KZTFPCzczckoo/edit?usp=sharing"
        # conn = connect()
        # rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
        # df_gsheet = pd.DataFrame(rows)
        # st.write(df_gsheet)

       #############
        # df=pd.read_csv('dataset.csv')
        
        # sheet_id = "16ciPmGxI4p6_a1VdE1lwNNplm1OF0-KZTFPCzczckoo"

        # df_gsheet = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
        # # st.write(df)
        # st.write(df_gsheet)

        #conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
        @st.cache(suppress_st_warning=True,ttl=1)
        def myfunctions(query):
        #sheet_id = "16ciPmGxI4p6_a1VdE1lwNNplm1OF0-KZTFPCzczckoo"
        #df_gsheet = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
              # # st.write(df)
            df_gsheet = pd.read_csv(f"{query}")
            st.write(df_gsheet)

    sheet_url = st.secrets["public_gsheets_url"]
    myfunctions(f'{sheet_url}')

    #myfunctions()



    # def run_query(query):
    #     rows = conn.execute(query)
    #     rows = rows.fetchall()
    #     return rows

    # sheet_url = st.secrets["public_gsheets_url"]
    # df_gsheet = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_url}/export?format=csv")
    # rows = run_query(f'SELECT * FROM "{df_gsheet}"')

    # df_gsheet = pd.DataFrame(rows)
    # st.write(df_gsheet)

    with co3:
        st.write("")
    
    #st.plot()
    st.write("")
    sheet_id = "16ciPmGxI4p6_a1VdE1lwNNplm1OF0-KZTFPCzczckoo"
    df_gsheet = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    df_humid = df_gsheet['Humidity (%)'].iloc[-1]
    df_temp = df_gsheet['Temperature (*C)'].iloc[-1]
    df_gas = df_gsheet['Gas (ppm)'].iloc[-1]
    df_date = df_gsheet['Date'].iloc[-1]
    df_time = df_gsheet['Time'].iloc[-1]
    st.write("")
    st.write("Latest Data : On {} at {} the food Humidity (%) is {} , Temperature (*C) is {} & Gas (ppm) is {}".format(df_date,df_time,df_humid,df_temp,df_gas))

    st.write("")

    st.title("Combined Graph Information")

    col1, col2, col3 = st.columns([0.8,6,0.8])


    with col1:
        st.write("")

    
    with col2:
        st.write("")
    
    with col3:
        st.write("")




    # html_gas = """
    # <div style="background-color:Red;padding:30px">
    # <h2 style="color:white;text-align:center;">Real </h2>
    # </div>
    # """
    
    # st.write("THE K-NN Analysis")
    # img = Image.open('images/download.png')
    # st.image(img,width=600,caption='10-NN Cluster Analysis on Air_Quality')

    # st.markdown(html_gas,unsafe_allow_html=True)

    # st.write("")
    # st.write("")
    # st.write("")

    # gas_b = st.text_input("GAS_DATA","Type Here")
    
    # result_g=""
    # if st.button("FOOD QUALITY"):
    #     result_g=predict_gas(gas_b)
    # st.success('The output is {}'.format(result_g))    

    # st.write("")
    # st.write("")    
    # st.write("")


if __name__=='__main__':
    main()
