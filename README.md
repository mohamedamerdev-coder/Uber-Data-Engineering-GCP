#  Uber Data Analytics | End-to-End Data Engineering Project

##  Project Overview
This project aims to build a comprehensive ETL pipeline for Uber trip data. The goal is to extract raw data, transform it into a structured Data Model, and load it into a Cloud Data Warehouse for analysis and visualization.

**Status:** `Work In Progress (WIP)` - Phase 1 (Data Modeling & Transformation) Completed.

## Architecture & Tech Stack
- **Programming Language:** Python
- **Transformation:** Pandas (Data Cleaning & Dimensional Modeling)
- **Orchestration:** Mage.ai (Planned)
- **Cloud Storage:** Google Cloud Storage (GCS) (Planned)
- **Data Warehouse:** BigQuery (Planned)
- **Visualization:** Looker Studio (Planned)

## What has been done so far?
### Phase 1: Data Modeling & Transformation 
- Analyzed the raw dataset and designed a **Star Schema** (Fact & Dimension Tables).
- Built the **Data Model** using `Lucidchart`.
- Developed Python scripts using `Pandas` to:
  - Clean the raw data (handling duplicates, formatting datetime).
  - Create Dimension Tables: `datetime_dim`, `passenger_count_dim`, `trip_distance_dim`, `rate_code_dim`, etc.
  - Create the Fact Table (`fact_table`) by merging dimensions.
  - <img width="1165" height="829" alt="Screenshot 2025-12-14 231413" src="https://github.com/user-attachments/assets/bc0881e9-6116-47b0-be52-aeba308ecd89" />


## Next Steps
- Deploying the transformation code to **Mage.ai**.
- Setting up **Google Cloud Storage (GCS)** for raw data ingestion.
- Loading the transformed data into **BigQuery**.
- Building the final Dashboard on **Looker Studio**.

---
*Developed by [Mohamed Amer]*
