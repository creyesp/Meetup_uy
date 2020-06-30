from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import joblib
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np
import streamlit as st


import streamlit as st
import pandas as pd
import numpy as np

st.title('Princing')

# @st.cache
def load_model(path):
    model = joblib.load(path)
    return model

data_load_state = st.text('Loading model...')
model = load_model('/home/cesar/Projects/personal/Meetup_uy/models/rfc_model.joblib')
# data_load_state.text("Done!")

st.subheader('Number of pickups by hour')
# Some number in the range 0-23
bathrooms = st.slider('bathrooms', 1, 3, 1)
bedrooms = st.slider('bedrooms', 0, 3, 1)
servide_fees = st.slider('servide_fees', 0, 50000, 1000)

st.write(f'Price predicted: {int(model.predict(sample)[0]):,}')