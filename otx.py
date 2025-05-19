import httpx, os
async def fetch_otx():
    api_key = os.getenv("OTX_API_KEY")
    headers = {"X-OTX-API-KEY": api_key}
    url = "https://otx.alienvault.com/api/v1/indicators/export"
    # Example: fetch recent IOC indicators
    resp = httpx.get(url, headers=headers, timeout=10.0)
    # Parse resp.json() to extract IOCs
    return [("example.com", "domain")]
