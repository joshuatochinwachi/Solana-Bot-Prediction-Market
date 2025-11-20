import os
import requests
import joblib
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

dune_api_key = os.getenv("DEFI_JOSH_DUNE_QUERY_API_KEY")

query_ids = [
    "4422946",

    "4870857",
    "4870877",
    "4870869",
    "4870897",
    "4870936",
    "4870883",
    "5147816",
    "4875976",
    "4870860",
    "4870931",
    "5817379",
    "4870903",
    "4870941",
    "4870926",
    "4870880",
    "4940212",
    "5028367",
    "4870929",

    "4999410",
    "5331040",
    "4636621",
    "4079468",
    "4044367",
    "4962800",
    "4608470",
    "3939570",
    "3958821",
    "4023198",
    "4022970",
    "4023155",
    "4966713",
    "4897401",
    "4043813",
    "5325489",
    "4966625",

    "4909271",
    "4835076",
    "4909584",
    "4835099",
    "5149402",
    "5817400",
    "4835191",
    "5149469",
    "5325494",
    "5149452",
    "4835097"
]

os.makedirs("data", exist_ok=True)

for query_id in query_ids:
    print(f"\nFetching data for query ID: {query_id}")
    
    url = f"https://api.dune.com/api/v1/query/{query_id}/results/csv"
    headers = {"X-DUNE-API-KEY": dune_api_key}
    
    joblib_file = f"data/query_{query_id}_data.joblib"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        
        query_data = {
            "query_id": query_id,
            "data": response.text,
            "last_updated": datetime.now().isoformat(),
            "status": "success"
        }
        
        joblib.dump(query_data, joblib_file)
        
        print(f"✓ Successfully fetched and saved query {query_id} to {joblib_file}")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Error fetching query {query_id}: {e}")
        
        query_data = {
            "query_id": query_id,
            "data": None,
            "last_updated": datetime.now().isoformat(),
            "status": f"error: {str(e)}"
        }
        joblib.dump(query_data, joblib_file)

print("\n✓ All queries processed")