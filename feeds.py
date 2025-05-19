import asyncio
from .otx import fetch_otx
from .shodan import fetch_shodan
from .censys import fetch_censys
from .virustotal import fetch_virustotal

async def fetch_all_iocs():
    tasks = [
        fetch_otx(),
        fetch_shodan(),
        fetch_censys(),
        fetch_virustotal()
    ]
    results = await asyncio.gather(*tasks)
    # Flatten and return list of (value, type)
    iocs = [ioc for sublist in results for ioc in sublist]
    return iocs
