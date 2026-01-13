# project: hotel-booking-etl-pipeline 🔒
> **status:** architecting secure data infrastructure
> **stack:** python, pandas, sqlite, [aspiring: airflow & aws iam]

01. overview
this project demonstrates a full **etl (extract, transform, load)** pipeline designed for high-integrity data environments. it transforms raw, messy hotel booking logs into a structured, query-ready sql database.

02. the pipeline
- **extract:** automated ingestion from kagglehub api to ensure environment reproducibility.
- **transform:** engineered data cleaning logic in pandas—removing high-null columns (company), imputing agent/children data, and enforcing deduplication.
- **load:** structured ingestion into a relational sqlite database for persistent, high-speed querying.

03. architect notes (security pivot)
to maintain an "untouchable" infrastructure, this pipeline is being evolved to include:
- **orchestration:** scheduling via airflow to automate daily 08:00 refresh cycles.
- **security:** implementing iam (identity & access management) roles to enforce least-privilege access to the data sink.

04. features
- Clean CSVs with Pandas.
- Remove duplicates, fix formats automatically.
- Generate summary statistics.
- Visualize data distributions with Matplotlib.
- Export cleaned data to new CSV files.

05. how to run
1. clone the repo.
2. run `pip install -r requirements.txt`.
3. execute `dataa_.ipynb` to generate `hotel_bookings.db`.

extra:
- Add a hotel recommendation mode around it so the model can suggest hotels and places based on user preferences from the cleaned data.
Your current project is a perfect ETL (Extract, Transform, Load) project.

