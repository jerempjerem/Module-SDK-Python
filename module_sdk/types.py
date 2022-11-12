from typing import TypedDict, Optional

# GENERAL
class SortDirection():
  priceAsc: str = 'priceAsc'
  priceDesc: str = 'priceDesc'
  timeAsc: str = 'timeAsc'
  timeDesc: str = 'timeDesc'

class Marketplace():
  all: str = 'all'
  Opensea: str = 'Opensea'
  LooksRare: str = 'LooksRare'
  X2Y2: str = 'X2Y2'

class OrderBy():
  volume: str = 'volume'
  saleCount: str = 'saleCount'
  price: str = 'price'

class TimeRange():
  all: str = 'all'
  day: str = 'day'
  week: str = 'week'
  month: str = 'month'

class OrderSource():
  Opensea_Wyvern: str = 'Opensea: Wyvern'
  Opensea_Wyvern_V1: str = 'Opensea: Wyvern V1'
  Opensea_Seaport: str ='Opensea: Seaport'
  LooksRare: str = 'LooksRare'
  X2Y2: str = 'X2Y2'

class OrderSide():
  ask: str = 'ask'
  bid: str ='bid'

class Aggregator():
  Gem_XYZ: str = 'Gem.XYZ'
  Genie: str = 'Genie'

class Type():
  all: str = 'all'
  ERC721: str = 'ERC721'
  ERC720: str ='ERC720'

InType = 'all' or 'transfer' or 'mint' or 'buy'
OutType = 'all' or 'transfer' or 'sale'

class Color():
    ERROR: str = 'red'


# ETHEREUM
class GetFullTX(TypedDict):
    count: Optional[int]
    offset:  Optional[int]
    txHash:  Optional[str]
    contractAddress: Optional[str]
    from_: Optional[str] # from
    to: Optional[str]
    blockNumber: Optional[int]
    sortDirection: Optional[SortDirection]

class GetBlock(TypedDict):
    blockNumber: Optional[int]
    count:  Optional[int]
    offset:  Optional[int]
    blockHash: Optional[str]
    sortDirection: Optional[SortDirection]

class GetTransactionReciept(TypedDict):
    count: Optional[int]
    offset:  Optional[int]
    txHash:  Optional[str]
    from_: Optional[str] # from
    to: Optional[str]
    blockNumber: Optional[int]
    sortDirection: Optional[SortDirection]

class GetTransaction (TypedDict):
    count: Optional[int]
    offset:  Optional[int]
    txHash:  Optional[str]
    from_: Optional[str] # from
    to: Optional[str]
    blockNumber: Optional[int]
    sortDirection: Optional[SortDirection]

# NFT
class GetCollectionInfo(TypedDict):
  contractAddress: Optional[str]
  slug: Optional[str]

class GetCollectionStats(TypedDict):
  contractAddress: Optional[str]
  slug: Optional[str]
  marketplace: Optional[Marketplace]

class GetCollectionRankings(TypedDict):
  orderBy: Optional[OrderBy]
  timeRange: Optional[TimeRange]
  count: Optional[int]
  offset: Optional[int]
  marketplace: Optional[Marketplace]

class GetListings(TypedDict):
  active: Optional[bool]
  count: Optional[int]
  offset: Optional[int]
  sortDirection: Optional[SortDirection]
  marketplace: Optional[Marketplace]
  slug: Optional[str]
  contractAddress: Optional[str]
  tokenId: Optional[str]
  withMetadata: Optional[bool]

class GetSales(TypedDict):
  count: Optional[int]
  offset: Optional[int]
  sortDirection: Optional[SortDirection]
  orderSource: Optional[OrderSource]
  orderSide: Optional[OrderSide]
  aggregator: Optional[Aggregator]
  contractAddress: Optional[str]
  slug: Optional[str]
  tokenId: Optional[str]
  from_: Optional[str] # from
  to: Optional[str]
  minPrice: Optional[str]
  maxPrice: Optional[str]
  withMetadata: Optional[bool]

class GetCollectionFloor(TypedDict):
  contractAddress: Optional[str]
  slug: Optional[str]

class GetTokenInfo(TypedDict):
  contractAddress: Optional[str]
  slug: Optional[str]
  tokenId: Optional[str]

class Token(TypedDict):
  tokenId: Optional[str]
  contractAddress: Optional[str]

class GetBatchTokenInfo(TypedDict):
  tokens: Optional[list[Token]]

class GetTokenOwner(TypedDict):
  contractAddress: Optional[str]
  slug: Optional[str]
  tokenId: Optional[str]

class GetTokensOwned(TypedDict):
  address: Optional[str]
  count: Optional[int]
  offset: Optional[int]
  type: Optional[Type]
  withMetadata: Optional[bool]
  contractAddress: Optional[str]

class GetCollectionsOwned(TypedDict):
  address: Optional[str]
  count: Optional[int]
  offset: Optional[int]
  type: Type
  withMetadata: Optional[bool]

class GetCollectionIntersection(TypedDict):
  contractAddressOne: Optional[str]
  contractAddressTwo: Optional[str]

class GetUserTradingStats(TypedDict):
  address: Optional[str]
  contractAddress: Optional[str]

class GetUserTradingHistory(TypedDict):
  address: Optional[str]
  contractAddress: Optional[str]
  count: Optional[int]
  offset: Optional[int]
  withMetadata: Optional[bool]
  in_type: Optional[InType]
  out_type: Optional[OutType]

class GetBatchUserTradingStats(TypedDict):
  addresses: Optional[str]

class GetCollectionSpread(TypedDict):
  contractAddress: Optional[str]

class GetMintVolume(TypedDict):
  contractAddress: Optional[str]
  slug: Optional[str]

# METADATA
class GetNFTMetadata(TypedDict):
  contractAddress: Optional[str]
  tokenId: Optional[str]

class GetContractABI(TypedDict):
  contractAddress: Optional[str]

class GetNFTMetadataSpread(TypedDict):
  contractAddress: Optional[str]


# CENTRAL
class ResolveCollection (TypedDict):
    term: Optional[str]
    count:  Optional[int]
    match:  Optional[bool]
    isVerified: Optional[SortDirection]