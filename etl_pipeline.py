import requests
import zipfile
import io
import boto3

# --- CONFIGURATION ---
DATA_URL = "https://cricsheet.org/downloads/ipl_json.zip"
AWS_BUCKET = "ipldwspipeline" 
AWS_ACCESS_KEY = "MY ACCESS KEY"       
AWS_SECRET_KEY = "MY SEQRET KEY"       
def run_pipeline():
    print("1. Downloading IPL Data...")
    try:
        r = requests.get(DATA_URL)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        print("   Download Successful.")
    except Exception as e:
        print(f"   Error downloading: {e}")
        return

    print("2. Connecting to AWS S3...")
    s3 = boto3.client('s3', 
                      aws_access_key_id=AWS_ACCESS_KEY,
                      aws_secret_access_key=AWS_SECRET_KEY)

    # We take the first 50 files for demonstration
    json_files = [f for f in z.namelist() if f.endswith('.json')][:50]
    
    print(f"3. Uploading {len(json_files)} files to S3...")
    for filename in json_files:
        file_content = z.read(filename)
        s3.put_object(Bucket=AWS_BUCKET, Key=f"raw_json/{filename}", Body=file_content)
        print(f"   Uploaded: {filename}")
        
    print("Pipeline Complete! Data is in S3.")

if __name__ == "__main__":
    run_pipeline()