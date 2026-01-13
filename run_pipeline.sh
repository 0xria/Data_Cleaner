#!/bin/bash

# --- [ria.sh] data pipeline orchestrator ---
echo "Starting ETL Pipeline... $(date)"

# 1. Run the Python script (the one you exported from your notebook)
echo "Step 1: Running Transformations..."
python3 dataa_.py

# 2. Check the Database to prove it worked
echo "Step 2: Validating Database..."
sqlite3 hotel_bookings.db "SELECT count(*) FROM bookings;"

echo "Pipeline Finished! ✅"