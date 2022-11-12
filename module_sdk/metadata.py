from .types import Color, GetContractABI, GetNFTMetadata
from .datasets import NFTMetadata, ContractABI

from httpx import Client
from httpx import TimeoutException, ConnectError
from termcolor import cprint

class Metadata():
    def __init__(self, client: Client) -> None:
        self.client = client

    def getNFTMetadata(self, parameters: GetNFTMetadata = {}) -> NFTMetadata:
        """
          Gets the metadata associated with the provided query and token.
        """

        try:
            response = self.client.get('/eth/metadata/getMetadata?', params=parameters)
            if response.status_code == 200:
                return response.json()['data']
            
            if response.json().get('error'):
                error = response.json().get('error')
                cprint(f'Module API Error: {error}', Color.ERROR)
                return
            cprint(f'Module API Unknown Error: {response}', Color.ERROR)
            return
        except TimeoutException:
            cprint(f'Module API Timeout Error', Color.ERROR)
        except ConnectError:
            cprint(f'Module API Connection Error', Color.ERROR)
        except Exception as e:
            cprint(f'Module API Error: {e}', Color.ERROR)

    def getContractABI(self, parameters: GetContractABI = {}) -> ContractABI:
        """
          Retrieve the ABI of a contract (ALPHA)
        """

        try:
            response = self.client.get('/eth/metadata/getABI?', params=parameters)
            if response.status_code == 200:
                return response.json()['data']
            
            if response.json().get('error'):
                error = response.json().get('error')
                cprint(f'Module API Error: {error}', Color.ERROR)
                return
            cprint(f'Module API Unknown Error: {response}', Color.ERROR)
            return
        except TimeoutException:
            cprint(f'Module API Timeout Error', Color.ERROR)
        except ConnectError:
            cprint(f'Module API Connection Error', Color.ERROR)
        except Exception as e:
            cprint(f'Module API Error: {e}', Color.ERROR)
