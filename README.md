# SQL Query Converter

## Overview
The SQL Query Converter is a Streamlit-based application that allows users to convert SQL queries written in Databricks format to other database platforms such as Teradata, Snowflakes, and Netezza. By uploading a datatype mapping Excel file, this tool makes it easy to adapt SQL queries to meet platform-specific requirements.

## How It Works
1. Upload an Excel file with datatype mappings.
2. Enter the SQL query in Databricks format.
3. Select the target database platform.
4. Generate the converted SQL query with a single click.

## Installation and Setup
### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Ngrok (optional, for external access)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd sql-query-converter
2. Install Dependencies:

pip install -r requirements.txt
3. Run the Application:

streamlit run app.py
Access the Application: Open your browser and go to http://127.0.0.1:8501.

## Excel File Format
The uploaded Excel file should contain the following columns:

Databricks Data Types
Teradata Data Types
Snowflakes Data Types
Netezza Data Types
