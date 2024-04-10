import pandas as pd
from sqlalchemy import create_engine



# Path to your Excel file
excel_file_path = 'C:/Users/HP/Desktop/Others-Raw.xlsx'

# PostgreSQL connection string
db_connection_str = 'postgresql://postgres:676108@localhost/test'

# Create a connection engine
engine = create_engine(db_connection_str)

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Truncate the table if it exists
with engine.connect() as con:
    con.execute('TRUNCATE TABLE others;')

# Append the DataFrame to the PostgreSQL table
df.to_sql('others', engine, if_exists='append', index=False)


