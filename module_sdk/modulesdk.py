from .utils.types import *
from .modules.ethereum import Ethereum
from .modules.central import Central
from .modules.nft import NFT
from .modules.metadata import Metadata

from httpx import Client


class Module():
    def __init__(self, api_key: str = None) -> None:

        client = Client(
            headers={
                'Content-Type': 'application/json',
                'X-API-KEY' : api_key if api_key else ''
            },
            timeout=1000,
            base_url='https://api.modulenft.xyz/api/v2/'
        )

        self.eth = Ethereum(client)
        self.metadata = Metadata(client)
        self.nft = NFT(client)
        self.central = Central(client)
