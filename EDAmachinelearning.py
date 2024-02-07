import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')
from matplotlib import pyplot as plt
from plotly import graph_objs as go
import seaborn as sns

st.set_page_config(page_title="OCD", page_icon=":bar_chart:",layout="wide")

st.title(" :bar_chart:  Explore Features Associated with Obsessive Complusive Disorder")

st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

#fl = pd.read_csv
#fl = st.file_uploader(":file_folder: Upload a file",type=(["csv","txt","xlsx","xls"]))
#show_file_uploader = st.checkbox("Show File Uploader")

#if fl is not None:
 #   filename = fl.name
    #st.write(filename)
   # df = pd.read_csv(filename, encoding = "ISO-8859-1")
#else:
os.chdir(r"/Users/user/Documents/machinelearning")
df = pd.read_csv("ocd_patient_dataset.csv", encoding = "ISO-8859-1")


#st.header("Car Market Snapshot")

col1,col2 = st.columns((2))
#df["Registration_Year"] = pd.to_(df["Registration_Year"])


#Calculate the average price based on the selected feature
#average_price = df.groupby(featur["Price"].mean()

# Plot the graph
#st.title("Average Price based on Selected Feature")
#st.bar_chart(average_price)
# Calculate the average price for each category


st.sidebar.header("Explore The OCD Patient Dataset: ")
# Create for gearbox region
depressiond = st.sidebar.multiselect("Pick Depression Diagnosis", df["Depression Diagnosis"].unique())
if not depressiond:
    df2 = df.copy()
else:
    df2 = df[df["Depression Diagnosis"].isin(depressiond)]

# Create for Body Type state
pvdiagnosis = st.sidebar.multiselect("Pick the Previous Diagnosis", df["Previous Diagnoses"].unique())
if not pvdiagnosis:
    df3 = df.copy()
else:
    df3 = df[df["Previous Diagnoses"].isin(pvdiagnosis)]


# Create for Body Type state
familyhistory = st.sidebar.multiselect("Family History of OCD", df["Family History of OCD"].unique())
if not familyhistory:
    df4 = df.copy()
else:
    df4 = df[df["Family History of OCD"].isin(familyhistory)]
    

# Create for Body Type state
#depressiondiagnosis = st.sidebar.multiselect("Pick Depression Diagnosis", df["Depression Diagnosis"].unique())
#if not depressiondiagnosis:
 #   df5 = df.copy()
#else:
 #   df5= df[df["Depression Diagnosis"].isin(depressiondiagnosis)]


 

# Create for Engine size city
#enginesize  = st.sidebar.multiselect("Pick Family History of OCD"),df3["Family History of OCD"].unique()

# Create for Emmision size city
#fueltype  = st.sidebar.multiselect("Pick the Fuel Type",df3["Fuel type"].unique())


if not depressiond and not pvdiagnosis and not familyhistory :
    filtered_df = df
elif not pvdiagnosis and not familyhistory:
    filtered_df = df[df["Depression Diagnosis"].isin(depressiond)]
elif not depressiond and not familyhistory:
    filtered_df = df[df["Previous Diagnoses"].isin(pvdiagnosis)]
elif not familyhistory and not pvdiagnosis:
     filtered_df = df[df['Depression Diagnosis'].isin(depressiond)]
elif  depressiond and pvdiagnosis:
    filtered_df =  df[df["Depression Diagnosis"].isin(depressiond) & df["Previous Diagnoses"].isin(pvdiagnosis)] 

#elif  bodytype and fueltype:
  #  filtered_df =  df[df["Body type"].isin(bodytype) & df["Fuel type"].isin(fueltype)]      
elif  pvdiagnosis and familyhistory:
    filtered_df =  df[df["Previous Diagnoses"].isin(pvdiagnosis) & df["Family History of OCD"].isin(familyhistory)]
elif depressiond and familyhistory:
    filtered_df = df3[df["Depression Diagnosis"].isin(depressiond) & df3["Family History of OCD"].isin(familyhistory)]
elif depressiond and pvdiagnosis:
    filtered_df = df3[df["Depression Diagnosis"].isin(depressiond) & df3["Previous Diagnoses"].isin(pvdiagnosis)]
#elif depressiond and pvdiagnosis:
 #   filtered_df = df3[df["Depression Diagnosis"].isin(depressiond) & df3["Previous Diagnosis"].isin(pvdiagnosis)]
#elif fueltype:
 #   filtered_df = df3[df3["Fuel type"].isin(fueltype)] 
elif familyhistory:
    filtered_df = df3[df3["Family History of OCD"].isin(familyhistory)]

else:
    filtered_df = df[df2["Depression Diagnosis"].isin(depressiond) & df2["Previous Diagnoses"].isin(pvdiagnosis)]
   
   
obessiontype_df = filtered_df.groupby(by = ["Obsession Type"], as_index = False)["Age"].mean()
compulsiontype_df = filtered_df.groupby(by = ["Compulsion Type"], as_index = False)["Patient ID"].count()
compulsiontype_df2 = filtered_df.groupby(by = ["Compulsion Type"], as_index = False)["Age"].mean()
depression_df = filtered_df.groupby(by = ["Depression Diagnosis"], as_index = False)["Patient ID"].count()
anxiety_df=  filtered_df.groupby(by =["Anxiety Diagnosis"], as_index = False)["Patient ID"].count()
ycomplusion_df= filtered_df.groupby(by =["Y-BOCS Score (Obsessions)"], as_index = False)["Patient ID"].count()
ycomplusion2_df= filtered_df.groupby(by =["Y-BOCS Score (Compulsions)"], as_index = False)["Patient ID"].count()
medication_df= filtered_df.groupby(by =["Medications"], as_index = False)["Patient ID"].count()
#fueltype_df= filtered_df.groupby(by =["Fuel type"], as_index = False)["Price"].mean()
#emissiontype_df= filtered_df.groupby(by =["Emission Class"], as_index = False)["Price"].mean()
with col1:
    st.subheader("Depression Diagnosis")
    if not depression_df.empty:
        fig = px.pie(depression_df, values="Patient ID", names="Depression Diagnosis", hole=0.4)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data available for the selected filters.")

with col2:
    st.subheader("Anxiety Diagnosis")
    if not anxiety_df.empty:
        fig = px.pie(anxiety_df, values="Patient ID", names="Anxiety Diagnosis", hole=0.4)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data available for the selected filters.")


with col1:
    st.subheader("Compulsion Type by Patients")
    fig = px.bar(compulsiontype_df, x = "Compulsion Type", y = "Patient ID",
                 template = "seaborn",color_continuous_scale='reds')
    st.plotly_chart(fig,use_container_width=True, height = 200)
    

    
with col2:
    st.subheader("Average Age and  Obsession Type ")
    #fig = px.pie(brands_df, values = "Price", names = "Brand", hole = 0.5)
    fig = px.line(compulsiontype_df2, x = "Compulsion Type", y = "Age", markers = True)
    #fig = px.line(obessiontype_df, x= "Obsession Type", y = "Patient ID", markers = True)
   # fig.update_traces(text = obessiontype_df["Obsession Type"], textposition = "outside")
    st.plotly_chart(fig,use_container_width=True)
    
with col1:
    st.subheader("Y -BOCS Score (Obsessions) in Patients")
    #fig = px.pie(brands_df, values = "Price", names = "Brand", hole = 0.5)
    fig = px.bar(filtered_df, x= "Y-BOCS Score (Obsessions)", y = "Patient ID", color = "Obsession Type")
   # fig.update_traces(text = obessiontype_df["Obsession Type"], textposition = "outside")
    st.plotly_chart(fig,use_container_width=True)

with col2:
    st.subheader("Prescribed Medication")
    if not medication_df.empty:
        fig = px.bar(medication_df, title="OCD Diagnosis by Medication", x="Medications", y="Patient ID")
        st.plotly_chart(fig, use_container_width=True, height=200)
    else:
        st.warning("No data available for the selected filters.")
    

with col1:
    st.subheader("Y -BOCS Score (Compulsions) in Patients")
    #fig = px.pie(brands_df, values = "Price", names = "Brand", hole = 0.5)
    fig = px.bar(filtered_df, x= "Y-BOCS Score (Compulsions)", y = "Patient ID", color = "Compulsion Type")
   # fig.update_traces(text = obessiontype_df["Obsession Type"], textposition = "outside")
    st.plotly_chart(fig,use_container_width=True)

#with col2:
 #   st.subheader ("")
   #sns.set(style="whitegrid")
  # reg_plot = sns.regplot(x='Ethnicity', y='Depression Diagnosis', data=filtered_df)
   #st.pyplot(reg_plot.figure)