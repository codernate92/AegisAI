import httpx, os
async def fetch_censys():
    uid = os.getenv("CENSYS_UID")
    secret = os.getenv("CENSYS_SECRET")
    url = "https://search.censys.io/api/v2/hosts/search"
    resp = httpx.post(url, auth=(uid, secret), json={"query":"services.ssh.banner: OpenSSH"})
    data = resp.json()
    return [(hit['ip'], 'ip') for hit in data.get('result', {}).get('hits', [])]
