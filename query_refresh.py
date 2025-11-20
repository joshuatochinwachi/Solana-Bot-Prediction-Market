import os
import requests
from dotenv import load_dotenv

load_dotenv()
dune_api_key = os.getenv("DEFI_JOSH_DUNE_QUERY_API_KEY")

query_ids = [
        4422946,

        4870857,
        4870877,
        4870869,
        4870897,
        4870936,
        4870883,
        5147816,
        4875976,
        4870860,
        4870931,
        5817379,
        4870903,
        4870941,
        4870926,
        4870880,
        4940212,
        5028367,
        4870929,

        4999410,
        5331040,
        4636621,
        4079468,
        4044367,
        4962800,
        4608470,
        3939570,
        3958821,
        4023198,
        4022970,
        4023155,
        4966713,
        4897401,
        4043813,
        5325489,
        4966625,

        4909271,
        4835076,
        4909584,
        4835099,
        5149402,
        5817400,
        4835191,
        5149469,
        5325494,
        5149452,
        4835097
        ]

headers = {"X-DUNE-API-KEY": dune_api_key}

for query_id in query_ids:
    url = f"https://api.dune.com/api/v1/query/{query_id}/execute"
    response = requests.post(url, headers=headers)
    print(f"Query {query_id}: {response.text}")