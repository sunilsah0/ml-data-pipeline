from great_expectations.dataset import PandasDataset
import pandas as pd

df = pd.read_parquet("data/features/")

dataset = PandasDataset(df)

print("🔍 Running data quality checks...")
result = dataset.expect_column_values_to_be_between(
    "avg_spent", min_value=0, max_value=500
)

if result.success:
    print("✅ Data quality check passed")
else:
    print("❌ Data quality check failed")
