import streamlit as st
import snowflake.connector
import pandas as pd

# --- CONFIGURATION ---
# Snowflake details
USER = 'MYUSER'
PASSWORD = 'MYPASSWORD'
ACCOUNT = 'MYACCOUNT.snowflakecomputing.com' 

st.set_page_config(page_title="IPL Analytics", layout="wide")
st.title("🏏 IPL Data Engineering Dashboard")
st.markdown("### Powered by AWS, Snowflake & Python")

# Connect to Snowflake
@st.cache_resource
def get_data():
    ctx = snowflake.connector.connect( 
        
        user=USER,
        password=PASSWORD,
        account=ACCOUNT,
        warehouse='COMPUTE_WH', 
        database='IPL_DB',
        schema='RAW'
        
    )
    query = "SELECT * FROM FACT_BATTER_STATS ORDER BY TOTAL_RUNS DESC LIMIT 10"
    df = pd.read_sql(query, ctx)
    ctx.close()
    return df

try:
    df = get_data()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Top 10 Batsmen")
        st.dataframe(df)
        
    with col2:
        st.subheader("Run Scoring Chart")
        st.bar_chart(df.set_index("BATTER")['TOTAL_RUNS'])
        
except Exception as e:
    st.error(f"Error connecting to Snowflake: {e}")