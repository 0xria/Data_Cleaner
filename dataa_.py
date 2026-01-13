# %% [markdown]
# *project:* hotel booking data analysis/cleaning
# *data source:* https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand by Jesse Mostipak
# *accessed by me:* january 2026
# *purpose:* practice data cleaning and analysis using pandas in python and to identify cleaning patterns for cloud security log simulation..

# %%
#import libraries/dependencies
import kagglehub
import pandas as pd
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()  # Load the secret keys from .env file
os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')

print("--- Key loaded ✅ ---")
# 1. Download the dataset and get folderpath
dataset = kagglehub.dataset_download("jessemostipak/hotel-booking-demand")

# 2. List files in that dataset to find the exact CSV name
dataset_path = dataset  # assign the downloaded path to dataset_path
print("files in dataset folder:", os.listdir(dataset_path))

# 3. Add the CSV file path
csv_path = os.path.join(dataset_path, "hotel_bookings.csv")

# 4. NOW read it in
hotel_bookings = pd.read_csv(csv_path)

# 5. Check the result
print("--- successfully read in dataset ---")
hotel_bookings.head()

# %%
#read in dataset
hotel_bookings = pd.read_csv(csv_path)

# %%
#first look at dataset
hotel_bookings

# %%
# 1. Aggregate lost values per column
print("-- missing values report --")
print(hotel_bookings.isnull().sum())

# 2. Aggregate duplicate rows
print("\n-- duplicate rows report --")
print(f"total duplicates: , {hotel_bookings.duplicated().sum()}")

# %%
#1 drop 'company' column : high missing values
hotel_bookings.drop(columns=['company'], inplace=True, errors='ignore')

#2 fill missing values 'agent' and 'children' with 0
hotel_bookings['agent'] = hotel_bookings['agent'].fillna(0)
hotel_bookings['children'] = hotel_bookings['children'].fillna(0)

#3 drop duplicate rows
hotel_bookings.drop_duplicates(inplace=True)

print("--- Data Cleaning Done ✅ ---")

# %%
#1 . Create/connect to SQLite database
conn = sqlite3.connect('hotel_bookings.db')

#2 . Write & load DataFrame to SQL table and replace if exists
hotel_bookings.to_sql('bookings', conn, if_exists='replace', index=False)

print("--- Data Loaded into SQLite Database ✅ ---")

#3 . Close the connection
conn.close()


# %%
conn = sqlite3.connect('hotel_bookings.db')

query = "SELECT hotel, lead_time, arrival_date_year FROM bookings WHERE hotel = 'City Hotel' LIMIT 5"
df_from_sql = pd.read_sql(query, conn)

print(df_from_sql)
conn.close()


