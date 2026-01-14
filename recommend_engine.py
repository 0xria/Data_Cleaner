import sqlite3
import pandas as pd

def recommend_hotels(hotel_type, total_guests):
    conn = sqlite3.connect('hotel_bookings.db')

    query = """
    SELECT hotel, arrival_date_month, COUNT(*) as score
    FROM bookings
    WHERE is_canceled = 0 AND hotel = ? AND (adults + children +babies) >= ?
    GROUP BY arrival_date_month
    ORDER BY score DESC LIMIT 3
    """

    results = pd.read_sql(query, conn, params=(hotel_type, total_guests))

    if results.empty: #give global top months if no data found
        fallback_query = """
        SELECT hotel, arrival_date_month, COUNT(*) as score
        FROM bookings
        WHERE is_canceled = 0 
        GROUP BY arrival_date_month
        ORDER BY score DESC LIMIT 3
        """
        results = pd.read_sql(fallback_query, conn)
        results['note'] = "Showing popular overall (no specific match found)"

    conn.close()
    return results