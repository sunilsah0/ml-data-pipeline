# ml-data-pipeline
Project Overview

This project demonstrates an end-to-end ML data pipeline, built from the perspective of a data engineer.
The pipeline ingests raw customer activity data (batch + streaming), applies transformations, stores curated features in a feature store, ensures data quality, and orchestrates workflows with Airflow.

Use Case: Predicting customer churn.

Batch ingestion: Historical customer profiles & transactions.

Streaming ingestion: Real-time customer events (logins, purchases).

Feature pipeline: Aggregates churn-related metrics (e.g., last login time, avg. spend).

Feature Store: Feast manages feature access for ML training & inference.
