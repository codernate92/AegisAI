import shodan, os
async def fetch_shodan():
    client = shodan.Shodan(os.getenv("SHODAN_API_KEY"))
    # Example: search for known malicious IPs
    res = client.search("port:22")
    return [(match['ip_str'], 'ip') for match in res['matches']]
