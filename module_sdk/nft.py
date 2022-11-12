from .types import Color, GetCollectionFloor, GetCollectionInfo, GetCollectionIntersection, GetCollectionRankings, GetBatchUserTradingStats
from .types import GetCollectionsOwned, GetCollectionSpread, GetCollectionStats, GetListings, GetMintVolume, GetSales
from .types import GetTokenInfo, GetTokenOwner, GetTokensOwned, GetUserTradingHistory, GetUserTradingStats


from .datasets import Collection, CollectionFloor, CollectionOwnerSpread, CollectionRanking, CollectionsOwned, BatchUserTradingStatistics
from .datasets import Listing, Sale, Statistics, TokenInfo, TokenOwner, TokensOwned, UserTradingHistory, UserTradingStatistics, MintVolume

from httpx import Client
from httpx import TimeoutException, ConnectError
from termcolor import cprint

class NFT():

    def __init__(self, client: Client) -> None:
        self.client = client

    def getCollectionInfo(self, parameters: GetCollectionInfo = {}) -> Collection:
        """
          Get the transaction reciept of a specified query
        """

        try:
            response = self.client.get('eth/nft/collection?', params=parameters)
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

    def getCollectionStats(self, parameters: GetCollectionStats = {}) -> Statistics:
        """
          Get the transaction reciept of a specified query
        """

        try:
            response = self.client.get('eth/nft/stats?', params=parameters)
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

    def getCollectionRankings(self, parameters: GetCollectionRankings = {}) -> list[CollectionRanking]:
        """
          Get the transaction reciept of a specified query
        """

        try:
            response = self.client.get('eth/nft/ranks?', params=parameters)
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

    def getListings(self, parameters: GetListings = {}) -> list[Listing]:
        """
          Get the transaction reciept of a specified query
        """

        try:
            response = self.client.get('eth/nft/listings?', params=parameters)
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

    def getSales(self, parameters: GetSales = {}) -> list[Sale]:
        """
          Get the transaction reciept of a specified query
        """

        try:
            response = self.client.get('eth/nft/listings?', params=parameters)
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

    def getCollectionFloor(self, parameters: GetCollectionFloor = {}) -> CollectionFloor:
        """
          Get the transaction reciept of a specified query
        """

        try:
            response = self.client.get('eth/nft/floor?', params=parameters)
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

    def getTokenInfo(self, parameters: GetTokenInfo = {}) -> TokenInfo:
        """
          Get the transaction reciept of a specified query
        """

        try:
            response = self.client.get('eth/nft/token?', params=parameters)
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

    def getTokenOwner(self, parameters: GetTokenOwner = {}) -> list[TokenOwner]:
        """
          Get the transaction reciept of a specified query
        """

        try:
            response = self.client.get('eth/nft/owner?', params=parameters)
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

    def getTokensOwned(self, parameters: GetTokensOwned = {}) -> list[TokensOwned]:
        """
          Get the transaction reciept of a specified query
        """

        try:
            response = self.client.get('eth/nft/owned?', params=parameters)
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

    def getCollectionsOwned(self, parameters: GetCollectionsOwned = {}) -> list[CollectionsOwned]:
        """
          Get the transaction reciept of a specified query
        """

        try:
            response = self.client.get('eth/nft/collectionsOwned?', params=parameters)
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

    def getCollectionIntersection(self, parameters: GetCollectionIntersection = {}) -> list[str]:
        """
          Get the transaction reciept of a specified query
        """

        try:
            response = self.client.get('eth/nft/intersection?', params=parameters)
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

    def getUserTradingStats(self, parameters: GetUserTradingStats = {}) -> UserTradingStatistics:
        """
          Get the transaction reciept of a specified query
        """

        try:
            response = self.client.get('eth/nft/userStats?', params=parameters)
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

    def getUserTradingHistory(self, parameters: GetUserTradingHistory = {}) -> list[UserTradingHistory]:
        """
          Get the transaction reciept of a specified query
        """

        try:
            response = self.client.get('eth/nft/userHistory?', params=parameters)
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

    def getBatchUserTradingStats(self, parameters: GetBatchUserTradingStats = {}) -> list[BatchUserTradingStatistics]:
        """
          Get the transaction reciept of a specified query
        """

        try:
            response = self.client.get('eth/nft/batchGetUserStats?', params=parameters)
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

    def getCollectionOwnerSpread(self, parameters: GetCollectionSpread = {}) -> list[CollectionOwnerSpread]:
        """
          Get the transaction reciept of a specified query
        """

        try:
            response = self.client.get('eth/nft/ownerDistribution?', params=parameters)
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

    def getMintVolume(self, parameters: GetMintVolume = {}) -> MintVolume:
        """
          Get the transaction reciept of a specified query
        """

        try:
            response = self.client.get('eth/nft/totalMintVolume?', params=parameters)
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
