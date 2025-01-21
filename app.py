with open("app.py", "w") as f:
    f.write("""
import streamlit as st
import pandas as pd

# Your datatype conversion function
def convert_query(input_query, target_platform, datatype_mapping):
    platform_columns = {
        "Teradata": "Teradata Data Types",
        "Snowflakes": "Snowflakes Data Types",
        "Netezza": "Netezza Data Types"
    }

    if target_platform not in platform_columns:
        return "Unsupported platform."

    target_column = platform_columns[target_platform]

    # Loop through the mapping and replace data types in the query
    for i, row in datatype_mapping.iterrows():
        databricks_type = row['Databricks Data Types']
        target_type = row[target_column]
        input_query = input_query.replace(databricks_type, target_type)

    return input_query

def run_streamlit():
    st.title("SQL Query Converter")

    # Step 1: Upload the Excel file
    uploaded_file = st.file_uploader("Upload Datatypes Excel file", type=["xlsx"])
    
    if uploaded_file is not None:
        # Step 2: Read the Excel file into a DataFrame
        datatype_mapping = pd.read_excel(uploaded_file)

        # Step 3: Get user inputs for query and target platform
        input_query = st.text_area("Input SQL Query (Databricks format)", height=200)
        
        target_platform = st.selectbox("Select Target Platform", ["Teradata", "Snowflakes", "Netezza"])
        
        # Step 4: Convert the query when button is pressed
        if st.button("Convert"):
            if input_query:
                converted_query = convert_query(input_query, target_platform, datatype_mapping)
                st.subheader("Converted Query:")
                st.code(converted_query, language='sql')
            else:
                st.error("Please provide an SQL query.")
    else:
        st.error("Please upload the Datatypes Excel file.")

run_streamlit()
    """)

# Step 4: Open the Ngrok tunnel to expose the Streamlit app
# This starts the Streamlit app and makes it available online via Ngrok
!nohup streamlit run app.py &
from pyngrok import ngrok
public_url = ngrok.connect(8501, "http")
print(f"Streamlit App running at: {public_url}")
