from .types import Color, GetFullTX, GetBlock, GetTransaction, GetTransactionReciept
from .datasets import FullTx, Block, Transaction, TransactionReciept

from httpx import Client
from httpx import TimeoutException, ConnectError
from termcolor import cprint

class Ethereum():

    def __init__(self, client: Client) -> None:
        self.client = client

    def getFullTX(self, parameters: GetFullTX = {}) -> list[FullTx]:
        """
          Get the transaction reciept of a specified query
        """

        try:
            response = self.client.get('/eth/fulltx?', params=parameters)
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

    def getBlock(self, parameters: GetBlock = {}) -> list[Block]:
        """
          Get a block from the ETH blockchain.
        """
        try:
            response = self.client.get('/eth/blocks?', params=parameters)
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

    def getTransactionReciept(self, parameters: GetTransactionReciept = {}) -> list[TransactionReciept]:
        """
          Get the transaction reciept of a specified query
        """

        try:
            response = self.client.get('/eth/txReceipt?', params=parameters)
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

    def getTransaction(self, parameters: GetTransaction = {}) -> list[Transaction]:
        """
          Get the transaction data of a specified query
        """
        try:
            response = self.client.get('/eth/tx?', params=parameters)
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
