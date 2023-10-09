from ballyregan import ProxyFetcher
from ballyregan.models import Protocols, Anonymities
from fp.fp import FreeProxy

def fetch_proxy():
    fetcher = ProxyFetcher()
    try:
        proxies = fetcher.get(
        limit=10,
        protocols=[Protocols.HTTP],
        anonymities=[Anonymities.ANONYMOUS],
        )
    except:
        print("No Anonymous proxies found. Switching to normal proxies ...") 
        proxies = fetcher.get(
        limit=10,
        protocols=[Protocols.HTTP],
        )
    return proxies

def fetch_free_proxy():
    try:
        proxies = FreeProxy(country_id=['US'], 
                            anonym=True,
                            elite=True
                            ).get()
    except:
        print("No Anonymous proxies found. Switching to normal proxies ...") 
        proxies = FreeProxy(country_id=['US']
                            ).get()
    return proxies
        