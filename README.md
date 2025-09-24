# ml-data-pipeline
Project Overview

This project demonstrates an end-to-end ML data pipeline, built from the perspective of a data engineer.
The pipeline ingests raw customer activity data (batch + streaming), applies transformations, stores curated features in a feature store, ensures data quality, and orchestrates workflows with Airflow.

Use Case: Predicting customer churn.

Batch ingestion: Historical customer profiles & transactions.

Streaming ingestion: Real-time customer events (logins, purchases).

Feature pipeline: Aggregates churn-related metrics (e.g., last login time, avg. spend).

Feature Store: Feast manages feature access for ML training & inference.

3. Tech Stack

Ingestion: Kafka, Python

Processing: Apache Spark, dbt

Storage: MinIO (local S3), Postgres/BigQuery

Feature Store: Feast

Data Quality: Great Expectations

Orchestration: Apache Airflow

Testing: Pytest + dbt tests

Deployment: Docker + docker-compose

4. Pipeline Steps

Data Generation

Synthetic generator produces fake customer profiles + streaming events.

Data Ingestion

Batch loader stores daily dumps into Raw Zone (S3).

Kafka producer streams events into Kafka topic.

Transformations

Spark jobs calculate churn features (recency, frequency, monetary value).

dbt transforms into star schema in warehouse.

Feature Store Integration

Feast registers features (customer_id, last_login, avg_purchase, churn_label).

Data Quality

Great Expectations validates schemas, nulls, and feature ranges.

Orchestration

Airflow DAG runs: ingest → transform → validate → update feature store.

Consumption

ML notebook shows how models can access features from Feast for training.

5. How to Run
# 🚀 ML Data Pipeline Capstone

An end-to-end **data engineering project** demonstrating:
- Batch ingestion (MinIO/S3)
- Streaming ingestion (Kafka)
- Transformations (Spark)
- Feature Store (Feast)
- Data Quality (Great Expectations)
- Orchestration (Airflow)
- Testing (Pytest + GitHub Actions)

## Run in GitHub Codespaces
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/YOURUSERNAME/ml-data-pipeline-capstone)

## Quickstart
```bash
docker-compose up -d
python data/synthetic_data_generator.py
python ingestion/batch_ingest.py
python transformations/feature_engineering.py
python quality_checks/validate.py

# Clone repo
git clone https://github.com/yourusername/ml-data-pipeline-capstone.git
cd ml-data-pipeline-capstone

# Start services (Kafka, Spark, Airflow, MinIO, Postgres)
docker-compose up -d

# Generate synthetic data
python data/synthetic_data_generator.py

# Trigger Airflow DAG
http://localhost:8080 (Airflow UI)

6. Results

Clean feature store with curated churn-related features.

Data quality reports (Great Expectations HTML docs).

Orchestrated pipeline visible in Airflow UI.

Example ML notebook pulling features from Feast.
