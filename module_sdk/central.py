from .types import Color, ResolveCollection
from .datasets import Resolved

from httpx import Client
from httpx import TimeoutException, ConnectError
from termcolor import cprint

class Central():
    def __init__(self, client: Client) -> None:
        self.client = client

    def resolveCollection(self, parameters: ResolveCollection = {}) -> dict[Resolved]:
        """
          Resolves a collection based on the provided terms.
        """
        try:
            response = self.client.get('central/utilities/search?', params=parameters)
            if response.status_code == 200:
                data = response.json()['data']
                return {
                    'search': data.get('search'),
                    'count': data.get('count'),
                    'collections': data.get('collections')
                }
            
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