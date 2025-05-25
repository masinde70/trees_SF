

```python
import pandas as pd          # Data manipulation library
import plotly.express as px  # Visualization library
import streamlit as st       # Web app framework

st.set_page_config(layout='wide')  # Use full width for layout
st.title("SF Trees")               # App title

# App description
st.write(
    """
    This app analyses trees in San Francisco using
    a dataset kindly provided by SF DPW. The dataset
    is filtered by the owner of the tree as selected
    in the sidebar!
    """
)

trees_df = pd.read_csv("trees.csv")                 # Load dataset
today = pd.to_datetime('today')                     # Current date
trees_df['date'] = pd.to_datetime(trees_df['date']) # Parse tree planting dates
trees_df['age'] = (today - trees_df['date']).dt.days # Compute tree age in days

unique_caretakers = trees_df["caretaker"].unique()  # All tree owners
owners = st.sidebar.multiselect("Tree Owner Filter", unique_caretakers) # Owner filter
graph_color = st.sidebar.color_picker("Graph Colors") # Color selector

if owners:
    trees_df = trees_df[trees_df["caretaker"].isin(owners)] # Filter by owner

df_dbh_grouped = pd.DataFrame(
    trees_df.groupby(["dbh"]).count()['tree_id']
)                    # Count trees by diameter (dbh)
df_dbh_grouped.columns = ['tree_count'] # Rename column

col1, col2 = st.columns(2)             # Split page into two columns

with col1:
    # Histogram: distribution of tree widths (dbh)
    fig = px.histogram(
        trees_df, 
        x=trees_df["dbh"],
        title="Tree Width",
        color_discrete_sequence=[graph_color]
    )
    fig.update_xaxes(title_text="Width")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Histogram: distribution of tree ages
    fig = px.histogram(
        trees_df,
        x=trees_df["age"], 
        title="Tree Age",
        color_discrete_sequence=[graph_color]
    )
    st.plotly_chart(fig, use_container_width=True)
```

