# 🚕 Uber End-to-End Data Engineering Project

### 🌟 Overview
This project is a comprehensive **End-to-End Data Engineering Pipeline** that transforms raw Uber trip data into actionable insights. Built as part of my journey as a Computer Science student at **Alamein International University (AIU)**, this project covers the entire data lifecycle: from cloud storage and orchestration to data modeling and visualization.

---

### 🏗️ Project Architecture
The pipeline follows a modern data stack approach:
1. **Data Source:** Raw Uber CSV data stored in **Google Cloud Storage (GCS)**.
2. **Orchestration:** **Mage AI** running on a **GCP Compute Engine (VM)** instance.
3. **Processing:** Data cleaning and transformation using **Python (Pandas)**.
4. **Data Modeling:** Designing a **Star Schema** with Fact and Dimension tables.
5. **Data Warehouse:** **Google BigQuery** for high-performance analytics.
6. **Final Layer:** Custom **SQL** joins for the analytics table.
7. **Visualization:** Interactive Dashboard built with **Google Looker Studio**.

> **[REPLACE THIS: Insert your Mage Pipeline Screenshot here]**

---

### 🛠️ Tech Stack
| Tool | Purpose |
| :--- | :--- |
| **Python** | Data Transformation & ETL Logic |
| **Mage AI** | Modern Data Pipeline Orchestration |
| **GCP (Compute Engine)** | Virtual Machine Hosting |
| **GCP (GCS)** | Raw Data Lake Storage |
| **BigQuery** | Cloud Data Warehousing |
| **SQL** | Analytics Table Construction |
| **Looker Studio** | BI & Dashboarding |

---

### 📉 Data Modeling (Star Schema)
To optimize query performance and maintain data integrity, the data was modeled into a **Star Schema**:

* **Fact Table:** `fact_table` (Measures and FKs).
* **Dimension Tables:** * `datetime_dim`
    * `passenger_count_dim`
    * `trip_distance_dim`
    * `rate_code_dim`
    * `pickup_location_dim`
    * `dropoff_location_dim`
    * `payment_type_dim`

---

### 🔥 Challenges Faced & Lessons Learned
Building this pipeline wasn't without its hurdles. Here’s how I tackled the technical challenges:

1.  **Environment Isolation (PEP 668):**
    * *Issue:* Encountered the `externally-managed-environment` error on Python 3.11 when installing GCP libraries.
    * *Fix:* Managed the installation using the `--break-system-packages` flag to ensure the VM environment had the necessary BigQuery SDKs.
2.  **Mage Exporter Logic:**
    * *Issue:* The initial exporter block attempted to iterate through columns as tables, causing `NameError` and `Table not found`.
    * *Fix:* Refactored the Python logic to correctly handle a dictionary of DataFrames, ensuring each dimension table was exported individually to BigQuery.
3.  **Geospatial Data Visualization:**
    * *Issue:* Looker Studio initially failed to recognize Latitude and Longitude fields.
    * *Fix:* Reconfigured the Data Source field types to **Geo** coordinates to enable the Map visualizations.

---

### 📊 Final Insights
The final analytics layer provides a deep dive into Uber's operations:
* **Revenue Analysis:** ~$1.6M total revenue processed.
* **Geospatial Mapping:** Identification of high-density pickup zones in New York.
* **Operational Efficiency:** Average trip distances and payment method preferences.

 **[Live Dashboard Link](https://lookerstudio.google.com/reporting/3bc1ef5c-a4a5-44c2-b80c-9fc2fdfa63d8)**
 
 <img width="668" height="798" alt="Screenshot 2026-01-09 172051" src="https://github.com/user-attachments/assets/52be53a9-997a-41de-82fc-87b537fe6538" />




 **Mohamed Amer**
