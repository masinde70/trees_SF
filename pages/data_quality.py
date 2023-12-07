import pandas as pd
import streamlit as st

st.title("SF Trees Data Quality App")
st.write(
    """
    This app is a data quality app for the SF Trees dataset.
    Edit the data and save to the new file!
    """
)

trees_df = pd.read_csv("trees.csv") # load data
trees_df = trees_df.dropna(subset=["longitude", "latitude"])
trees_df_filtered = trees_df[trees_df["legal_status"] == "Private"]
st.dataframe(trees_df)
edited_df = st.experimental_data_editor(trees_df_filtered)
trees_df.loc[edited_df.index] = edited_df
if st.button("Save Data and Overwrite"):
    trees_df.to_csv("trees.csv", index=False)
    st.success("Saved Data!")