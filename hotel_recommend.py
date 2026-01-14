import sqlite3
import pandas as pd

def recommend_hotels(hotel_type, total_guests):
    
    conn = sqlite3.connect('hotel_data.db') #connect db
    
    #Find successful bookings that match 
    # the user's specific guest count and hotel preference.
    query = """
    SELECT hotel, 
           arrival_date_month, 
           COUNT(*) as popularity_score
    FROM bookings
    WHERE is_canceled = 0 
      AND hotel = ? 
      AND (adults + children + babies) >= ?
    GROUP BY arrival_date_month
    ORDER BY popularity_score DESC
    LIMIT 5;
    """
    
    results = pd.read_sql(query, conn, params=(hotel_type, total_guests))
    conn.close()
    return results

# Test it!
print(recommend_hotels('City Hotel', 2))