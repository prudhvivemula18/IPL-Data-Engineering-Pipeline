# 🏏 IPL Data Engineering End-to-End Pipeline

## 📌 Project Overview
This project builds a scalable ETL (Extract, Transform, Load) pipeline that ingests raw cricket match data, processes it in the cloud, and creates an analytical dashboard. It mimics a real-world enterprise data architecture using **AWS, Snowflake, and Python**.

**Goal:** Transform unstructured JSON data into actionable insights (e.g., Strike Rates, Run Tally) for IPL players.

## 🏗️ Architecture
**Flow:** `Cricsheet (Source)` -> `Python (Extraction)` -> `AWS S3 (Data Lake)` -> `Snowflake (Data Warehouse)` -> `Streamlit (Analytics)`


## 🛠️ Tech Stack
* **Language:** Python (Pandas, Boto3)
* **Cloud Storage:** AWS S3 (Simple Storage Service)
* **Data Warehouse:** Snowflake (Standard Edition)
* **Transformation:** SQL (Lateral Flatten, Window Functions)
* **Visualization:** Streamlit

## 🚀 Key Features
* **Automated Ingestion:** Python script fetches zip files, extracts JSON, and uploads to AWS S3.
* **Schema-on-Read:** Utilized Snowflake's `VARIANT` data type to handle semi-structured JSON without pre-defining schemas.
* **Advanced SQL:** Flattened complex nested JSON arrays (Innings -> Overs -> Deliveries) using `LATERAL FLATTEN`.
* **Interactive Dashboard:** Built a Streamlit app to visualize Top Batsmen and performance metrics.

## 📈 How to Run
1.  Clone the repo:
    ```bash
    git clone [https://github.com/yourusername/IPL-Data-Engineering-Pipeline.git](https://github.com/yourusername/IPL-Data-Engineering-Pipeline.git)
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the ETL pipeline:
    ```bash
    python etl_pipeline.py
    ```
4.  Launch the Dashboard:
    ```bash
    streamlit run app.py
    ```
