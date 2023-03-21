import streamlit as st
import pandas as pd
import numpy as np
import json
from PIL import Image
import time

# with st.sidebar:
#    st.sidebar.header("Menu")
col1, col2 = st.columns([1, 5], gap="Large")
# Logo
image = Image.open("images/symbol.png")
with col1:
    st.image(image, caption="Pandemic Symbol", width=120)
with col2:
    st.title('2033 Necrovirus "Zombie" Outbreak Info')


city_df = pd.read_csv("data/basicZombieData.csv")
st.error(
    "**State of Emergency Declared**: All citizens are advised to stay indoors and avoid public places until further notice. Emergency responders and law enforcement will be patrolling the streets to maintain order and ensure public safety."
)

col1, col2 = st.columns(2)
col1.metric("Total Infected", "3,453,212", "282,564", delta_color="inverse")
col2.metric("Days Since First Infection", "20 Days")

st.bar_chart(city_df, x="City Name", y="Number of Infected")

with open("story.txt", "r+") as myfile:
    story = myfile.read()
with st.expander("Outbreak Synopsis"):
    st.write(story)

with st.container():
    option = st.selectbox(
        "City",
        (
            "Austin",
            "Chicago",
            "Columbus",
            "Dallas",
            "Fort Worth",
            "Houston",
            "Jacksonville",
            "Los Angeles",
            "New York City",
            "Philadelphia",
            "Phoenix",
            "San Antonio",
            "San Diego",
            "San Francisco",
            "San Jose",
        ),
    )
    if option:
        city_df2 = pd.read_csv("data/basicZombieData.csv", index_col="City Name")
        warning = city_df2.loc[option]["Response of Local Authorities"]
        with open("warnings.json", "r") as f:
            warning_info = json.load(f)
        warning_info = warning_info[warning]

        st.error("**{}**: {}".format(warning, warning_info))
        st.markdown(
            "<h1 style='text-align:center'>{}</h1>".format(option),
            unsafe_allow_html=True,
        )
        city_name = option.replace(" ", "")
        raw_line_df = pd.read_csv("data/" + city_name + ".csv")
        line_df = raw_line_df.set_index("Date")["Number of Infected"]
        city_col1, city_col2 = st.columns([10, 9])
        with city_col1:
            chart = st.line_chart(line_df[:1])
            # print(1)
            # print(line_df.iloc[[5]])
            # print(2)
            for i in range(1, len(line_df)):
                date = raw_line_df.iloc[[i]]["Date"].astype(str)
                infected = raw_line_df.iloc[[i]]["Number of Infected"].astype("int64")
                # print(new_line)

                chart.add_rows(
                    pd.DataFrame(
                        {"Date": date, "Number of Infected": infected}
                    ).set_index("Date")["Number of Infected"]
                )
                # chart.add_rows(new_line)
                time.sleep(0.05)
    with city_col2:
        st.image(
            "images/" + city_name + ".png",
        )

with open("disclaimer.txt", "r+") as myfile:
    disclaimer = myfile.read()

with st.expander("Disclaimer"):
    st.write(disclaimer)
# Access the warning for "State of Emergency Declared"
# state_of_emergency_warning = warnings["State of Emergency Declared"]
# print(state_of_emergency_warning)
