import boto3
import os

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="minio",
    aws_secret_access_key="minio123",
)

bucket = "raw-zone"

def upload_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)
    try:
        s3.create_bucket(Bucket=bucket)
    except:
        pass
    s3.upload_file(file_path, bucket, os.path.basename(file_path))
    print(f"✅ Uploaded {file_path} to {bucket}")

if __name__ == "__main__":
    upload_file("data/synthetic_events.json")
