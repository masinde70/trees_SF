import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')
st.title("SF Trees")
st.write(
    """
    This app analyses trees in San Francisco using
    a dataset kindly provided by SF DPW. The dataset
    is filtered by the owner of the tree as selected
    in the sidebar!
    """
)

trees_df = pd.read_csv("trees.csv") # load data
#st.write(trees_df.head()) # show data
today = pd.to_datetime('today') # get date
trees_df['date'] = pd.to_datetime(trees_df['date']) # convert to datetime
trees_df['age'] = (today - trees_df['date']).dt.days # calculate age
unique_caretakers = trees_df["caretaker"].unique() # get unique caretakers
owners = st.sidebar.multiselect("Tree Owner Filter", unique_caretakers)
graph_color = st.sidebar.color_picker("Graph Colors")

if owners:
    trees_df = trees_df[trees_df["caretaker"].isin(owners)] # filter by owner
df_dbh_grouped = pd.DataFrame(trees_df.groupby(["dbh"]).count()['tree_id']) # group by dbh
df_dbh_grouped.columns = ['tree_count'] # rename column

col1, col2 = st.columns(2)
with col1:
    fig = px.histogram(trees_df, x=trees_df["dbh"],
                        title="Tree Width",
                        color_discrete_sequence=[graph_color]
                        )
    fig.update_xaxes(title_text="Width")
    st.plotly_chart(fig, 
                    use_container_width=True)
    
 
with col2:
    fig = px.histogram(
        trees_df,
          x=trees_df["age"], 
        title="Tree Age",
        color_discrete_sequence=[graph_color])
    st.plotly_chart(fig, 
                    use_container_width=True)
 
    
