
from typing import Optional

# ETHEREUM
class Log():
  """
    Address associated with the transaction
  """
  address: str
  """
    Transaction block hash
  """
  blockHash: str
  """
    Transaction block number
  """
  blockNumber: int
  """
    Log data
  """
  data: str
  """
    Logs index
  """
  logIndex: int
  """
    Log removed flag
  """
  removed: bool
  """
    Transaction topic records
  """
  topics: list[str]
  """
    Transactions hash
  """
  transactionHash: str
  """
    Index of the transaction
  """
  transactionIndex: int

class FullTx():
  """
    Transactions unique hash
  """
  transactionHash: str
  """
    Block hash associated with the transaction
  """
  blockHash: str
  """
    Block number associated with the transaction
  """
  blockNumber: int
  """
    Contract address associated with the transaction
  """
  contractAddress: str
  """
    Cumulative gas used in this single transaction
  """
  cumulativeGasUsed: int
  """
    Sender address associated with the transaction
  """
  fromAddress: str
  """
    Gas used in this single transaction
  """
  gasUsed: int
  """
    Transaction event logs
  """
  logs: list[Log]
  """
    Transacition event logs bloom
  """
  logsBloom: str
  """
    Transaction status
  """
  status: str
  """
    Reciever address associated with the transaction
  """
  toAddress: str
  """
    Transaction index on the associated block
  """
  transactionIndex: int
  """
    Tx type of the transaction
  """
  txType: int
  """
    Transaction hash
  """
  hash: str
  """
    Transaction access list
  """
  accessList: list[str]
  """
    Chain Id associated with the transaction
  """
  chainId: int
  """
    Total gas used in the transaction
  """
  gas: int
  """
    Price of gas relative to the transaction
  """
  gasPrice: int
  """
    Input data of the transaction
  """
  input: str
  """
    Max price per gas relative to the transactions
  """
  maxFeePerGas: int
  """
    Max priority price per gas relative to the transaction
  """
  maxPriorityFeePerGas: int
  """
    Transaction nonce
  """
  nonce: int
  """
    Transaction ECDSA generator
  """
  r: str
  """
    Transaction ECDSA generator
  """
  s: str
  """
    Transaction ECDSA value
  """
  v: int
  """
    Value of the transaction
  """
  value: int

class Block():
  """
    Blocks hash
  """
  hash: str
  """
    Blocks base fee per gas
  """
  baseFeePerGas: str
  """
    Blocks overall difficulty
  """
  difficulty: int
  """
    Blocks extra data
  """
  extraData: str
  """
    Blocks marked gas limit
  """
  gasLimit: int
  """
    Blocks total gas used
  """
  gasUsed: int
  """
    Bloom of blocks logs
  """
  logsBloom: str
  """
    Miners address associated with the block
  """
  miner: str
  """
    Block mix hash
  """
  mixHash: str
  """
    Blocks one time nonce
  """
  nonce: str
  """
    Blocks "Block number"
  """
  number: int
  """
    Parent hash of the block
  """
  parentHash: str
  """
    Root of the blocks reciepts
  """
  recieptsRoot: str
  """
    Combined hash of all block uncles
  """
  sha3Uncles: str
  """
    Block size
  """
  size: int
  """
    Block state root
  """
  stateRoot: str
  """
    Blocks creation timestamp
  """
  timestamp: int
  """
    Blocks total mining difficulty
  """
  totalDifficulty: int
  """
    Blocks transacrion root
  """
  transactionRoot: str
  """
    Blocks uncles
  """
  uncles: list[str]

class Transaction():
  """
    Transaction hash
  """
  hash: str
  """
    Transaction access list
  """
  accessList: list[str]
  """
    Transaction block hash
  """
  blockHash: str
  """
    Block number of the transaction on chain
  """
  blockNumber: int
  """
    Chain ID associated with the transaction
  """
  chainId: str
  """
    Transctions sender address
  """
  fromAddress: str
  """
    Transactions total gas measure
  """
  gas: int
  """
    Transactions total gas price
  """
  gasPrice: int
  """
    Transaction input data
  """
  input: str
  """
    Transactions max fee per gas
  """
  maxFeePerGas: int
  """
    Transactions  max priority fee per gas
  """
  maxPriorityFeePerGas: int
  """
    Transaction one timed nonce
  """
  nonce: int
  """
    Transaction ECDSA generator
  """
  r: str
  """
    Transaction ECDSA generator
  """
  s: str
  """
    Transaction reciever address
  """
  toAddress: str
  """
    Transactions index on chain
  """
  transactionIndex: int
  """
    Transactions TX type
  """
  txType: int
  v: int
  """
    Transaction ECDSA
  """
  """
    Transaction value
  """
  value: int

class TransactionReciept():
  """
    Transactions hash on the blockchain
  """
  transactionHash: str
  """
    Transaction block hash
  """
  blockHash: str
  """
    Block number that contained the transaction
  """
  blockNumber: int
  """
    Contract address associated with the transaction
  """
  contractAddress: str
  """
    Measurable amount of gas used in this single transaction
  """
  cumulativeGasUsed: int
  """
    Sender address associated with the transaction
  """
  fromAddress: str
  """
    Measurable amount of gas used in this single transaction
  """
  gasUsed: int
  """
    Transaction logs
  """
  logs: list[Log]
  """
    Transaction log blooms
  """
  logsBloom: str
  """
    Transaction reciept status
  """
  status: str
  """
    Reciever address associated with the transaction
  """
  toAddress: str
  """
    Index of the transaction on the block
  """
  transactionIndex: int
  """
    TX type associated with the transaction
  """
  txType: int

# NFT

class Consideration():
  """
    Token address
  """
  token: str
  """
    Consideration item type
  """
  itemType: int
  """
    Consideration end amount
  """
  endAmount: str
  """
    Consideration receiver address
  """
  recipient: str
  """
    Consideration start amount
  """
  startAmount: str
  """
    Consideration type
  """
  identifierOrCriteria: str

class Offer():
  """
    Offers token address
  """
  token: str
  """
    Offers item type
  """
  itemType: int
  """
    Offers end amount
  """
  endAmount: str
  """
    Offers start amount
  """
  startAmount: str
  """
    Offers type
  """
  identifierOrCriteria: str

class ProtocolData():
  """
    Protocol salt
  """
  salt: str
  """
    Protocol zone
  """
  zone: str
  """
    Protocol offers(s)
    @type():Offer[]
  """
  offer: list[Offer]
  """
    Protocol ISO end time
  """
  endTime: str
  """
    Protocol counter
  """
  counter: int
  """
    Protocol zone hash
  """
  zoneHash: str
  """
    Protocol order type
  """
  orderType: int
  """
    Protocol ISO start time
  """
  startTime: str
  """
    Protocol conduit key
  """
  conduitKey: str
  """
    Protocol consideration(s)
    @type():Consideration[]
  """
  consideration: list[Consideration]
  """
    Protocols number of considerable items
  """
  totalOriginalConsiderationItems: int

class OrderData():
  """
    Orders unique hash
  """
  orderHash: str
  """
    Orders protocol data
    @type():ProtocolData;
  """
  protocolData: ProtocolData
  """
    Orders protocol address
  """
  protocolAddress: str

class FloorListing():
  """
    Listing identifier
  """
  id: str
  """
    Listing offerer address
  """
  offerer: str
  """
    Listed tokens address
  """
  tokenAddress: str
  """
    listed tokens identifier
  """
  tokenId: str
  """
    Listings price
  """
  priceAmount: str
  """
    Listings price currency
  """
  priceCurrency: str
  """
    Listings serving marketplace
  """
  marketplace: str
  """
    Listings ISO start time
  """
  startTime: str
  """
    Listings ISO endtime
  """
  endTime: str
  """
    Listings OrderData
    @type():OrderData
  """
  orderData: OrderData
  """
    Listings active status (listed/delisted)
  """
  active: bool

class CollectionFloor():
  price: str
  floorListing: FloorListing

class Socials():
  """
    Collections Telegram invite url
  """
  telegram_url: str
  """
    Collections Discord invite url
  """
  discord_url: str
  """
    Collections Twitter username
  """
  twitter_username: str
  """
    Collections Telegram invite url
  """
  medium_username: str
  """
    Collections Telegram invite url
  """
  wiki_url: str

class Images():
  """
    Collections primary image url
  """
  image_url: str
  """
    Collections large image url
  """
  large_image_url: str
  """
    Collections banner image url
  """
  banner_image_url: str
  """
    Collections featured image url
  """
  featured_image_url: str

class Fees():
  """
    Sellers fee address
  """
  sellerFeeAddress: str
  """
    Sellers listing fee
  """
  sellerFee: int
  """
    OpenSeas' listing fee
  """
  openseaFee: int
  """
    OpenSeas' fee address
  """
  openseaFeeAddress: str

class Collection():
  """
    Collection name
  """
  name: str
  """
    Collection symbol
  """
  symbol: str
  """
    Collection description
  """
  description: str
  """
    Collection contract address
  """
  contractAddress: str
  """
    Collection NSFW flag
  """
  is_nswf: bool
  """
    Collections verified flag (OpenSea ONLY)
  """
  verified: bool
  """
    Collections ERC token standard
  """
  ercType: str
  """
    Collections ISO creation date
  """
  createdDate: str
  """
    Contract socials
    @type():Socials
  """
  socials: Socials;
  """
    Collection images
    @type():Images
  """
  images: Images;
  """
    Collection fees
    @type():Fees
  """
  fees: Fees;

class FloorPrice():
  """
    Collection floor price in WEI
  """
  priceInWei: str
  """
    Collection floor price
  """
  price: str
  """
    Collections price currency type
  """
  priceCurrency: str
  """
    Collections floor listingfs
  """
  floorListing: FloorListing;

class Statistics():
  """
    Collection address
  """
  address: str
  """
    Collections all time activity volume
  """
  allTimeVolume: str
  """
    Collections daily activity volume
  """
  dailyVolume: str
  """
    Collections weekly activity volume
  """
  weeklyVolume: str
  """
    Collections all times sales count
  """
  allTimeSalesCount: str
  """
    Collections weekly sale count
  """
  weeklySalesCount: str
  """
    Collections monthly sales count
  """
  monthlySalesCount: str
  """
    Collections all time avg price in ETH
  """
  allTimeAveragePrice: str
  """
    Collections daily average price in ETH
  """
  dailyAveragePrice: str
  """
    Collections weekly average price in ETH
  """
  weeklyAveragePrice: str
  """
    Collections monthly average price in ETH
  """
  monthlyAverageprice: str
  """
    Collections floor price listings
    @type():FloorListing[]
  """
  floorPrice: FloorPrice;
  """
    Collections current listed token count
  """
  tokenListedCount: str
  """
    Collections total token supply count
  """
  totalSupply: str
  """
    Total token holders
  """
  holders: str

class Rankings():
  """
    Collection name
  """
  name: str
  """
    Collections slug
  """
  slug: str
  """
    Collection owner identifier
  """
  owner: int
  """
    Collection visibility flag (OpenSea/LooksRare)
  """
  hidden: bool
  """
    Collection symbol
  """
  symbol: str
  """
    Collection contract address
  """
  address: str
  """
    Collection NSWF flag (OpenSea/LooksRare)
  """
  is_nsfw: bool
  """
    Collection chat url
  """
  chat_url: str
  """
    Collection featured token url
  """
  featured: str
  """
    Collection wiki url
  """
  wiki_url: str
  """
    Collection image url
  """
  image_url: str
  """
    Collections seller fee in ETH
  """
  sellerFee: int
  """
    OpenSea collection fee in ETH
  """
  openseaFee: int
  """
    Collection description
  """
  description: str
  """
    Collection discord invite url
  """
  discord_url: str
  """
    Collections NFT versiont type
  """
  nft_version: str
  """
    Collection schema name
  """
  schema_name: str
  """
    Collection ISO creation date
  """
  created_date: str
  """
    Collections external website url
  """
  external_url: str
  """
    Collections telergram invite url
  """
  telegram_url: str
  """
    Collections secondary external website url
  """
  external_link: str
  """
    Collections require email flag (OpenSea/LooksRare)
  """
  require_email: bool
  """
    Collections payout address
  """
  payout_address: str
  """
    Collections default to fiat flag (OpenSea/LooksRare)
  """
  default_to_fiat: bool
  """
    Collections large image url
  """
  large_image_url: str
  """
    Collection medium article username
  """
  medium_username: str
  """
    Collections OpenSea creation version
  """
  opensea_version: str
  """
    Collection baner image url
  """
  banner_image_url: str
  """
    Collection seller fee address
  """
  sellerFeeAddress: str
  """
    Collection twitter username
  """
  twitter_username: str
  """
    Collection rarity flag (OpenSea/LooksRare)
  """
  is_rarity_enabled: bool
  """
    OpenSea collection fee address
  """
  openseaFeeAddress: str
  """
    Collection short description
  """
  short_description: str
  """
    Collection featured image url
  """
  featured_image_url: str
  """
    Collection instagram username
  """
  instagram_username: str
  """
    Collection token contract type
  """
  asset_contract_type: str
  """
    Collection only proxied transfers flag (OpenSea/LooksRare)
  """
  only_proxied_transfers: bool
  """
    Collection is subject to whitelist flag (OpenSea)
  """
  is_subject_to_whitelist: bool
  """
    Collection is safelist request status
  """
  safelist_request_status: str
  """
    Collection buyer fee points
  """
  opensea_buyer_fee_basis_points: str
  """
    Collection seller fee points
  """
  opensea_seller_fee_basis_points: str

class CollectionRanking():
  """
    Collection address
  """
  address: str
  """
    Collection all time activity volume
  """
  allTimeVolume: str
  """
    Collection daily activity volume
  """
  dailyVolume: str
  """
    Collection weekly activity volume
  """
  weeklyVolume: str
  """
    Collection all time sales count
  """
  allTimeSalesCount: str
  """
    Collection daily sales count
  """
  dailySalesCount: str
  """
    Collection weekly sales count
  """
  weeklySalesCount: str
  """
    Collection monthly sales count
  """
  monthlySalesCount: str
  """
    Collection total supply
  """
  totalSupply: int
  """
    Collections all time average price
  """
  allTimeAveragePrice: str
  """
    Collections daily price
  """
  dailyAveragePrice: str
  """
    Collections weekly average price
  """
  weeklyAveragePrice: str
  """
    Collections monthly average price
  """
  monthlyAveragePrice: str
  """
    Collections contract address
  """
  contractAddress: str
  """
    Collection rankings
    @type():Rankings[]
  """
  data: Rankings;

class Attributes():
  """
    Tokens attribute type
  """
  value: str
  """
    Tokens attribute value
  """
  trait_type: str

class Metadata():
  """
    Token name
  """
  name: str
  """
    Token image url
  """
  image: str
  """
    Token attributes
    @type():Attributes[]
  """
  attributes: list[Attributes]

class ListingsProtocolData():
  """
    Protocol signature.
  """
  signature: str
  """
    Protocol parameter data.
  """
  parameters: ProtocolData

class ListingsOrderData():
  """
    Listing order hash.
  """
  orderHash: str
  """
    Listings protocol data.
  """
  protocolData: ListingsProtocolData
  """
    Listings protocol address.
  """
  protocolAddress: str

class Listing():
  """
    Listing identifier
  """
  id: str
  """
    Listing offerer address.
  """
  offerer: str
  """
    Listings token address.
  """
  tokenAddress: str
  """
    Listings token id.
  """
  tokenId: str
  """
    Listings price amount.
  """
  priceAmount: str
  """
    List currency type.
  """
  priceCurrency: str
  """
    Marketplace the listing is active on.
  """
  marketplace: str
  """
    Start time of the listing.
  """
  startTime: str
  """
    End time of the listing.
  """
  endTime: str
  """
    Listing order data.
  """
  orderData: OrderData;
  """
    Listing active flag
  """
  active: bool
  """
    Token metadata.
  """
  metadata: Metadata;

class Sale():
  """
    Sale identifier.
  """
  id: str
  """
    Collection address.
  """
  contract: str
  """
    Tokens identifier.
  """
  token_id: str
  """
    Source of the orderer
  """
  order_source: str
  """
    Source of the filler.
  """
  fill_source: str
  """
    Source order side.
  """
  order_side: str
  """
    Filler order address.
  """
  from_address: str
  """
    Reciver order address.
  """
  to_address: str
  """
    sale price amount in ETH
  """
  amount: int
  """
    Sale transaction hash
  """
  txHash: str
  """
    Sale timestamp.
  """
  timestamp: str
  """
    Sale price in ETH.
  """
  sale_price_in_eth: str
  """
    Sale amount in ETH.
  """
  sale_amount: str
  """
    Sale assest type
  """
  sale_assest: str
  """
    Bundle flag
  """
  bundle: bool
  """
    Sale transaction block number.
  """
  block_number: int
  """
    ERC Schema type
  """
  erc: str
  """
    Token metadata.
  """
  metadata: Metadata;

class Floor():
  """
    Listing price in WEI
  """
  priceInWei: str
  """
    Listing price in ETH
  """
  price: str
  """
    Listing currency type
  """
  priceCurrency: str
  """
    Floor listings for collection
  """
  floorListing: list[FloorListing]

class UserTradingStatistics():
  """
    Users total mint volume
  """
  total_mint_volume: str
  """
    Users total buy volume
  """
  total_buy_volume: str
  """
    Users total buy quantity
  """
  total_buy_qty: str
  """
    Users total sell volume
  """
  total_sell_volume: str
  """
    Users total sell quantity
  """
  total_sell_qty: str
  """
    Users total mint gas costs
  """
  total_mint_gas_eth: str
  """
    Users total sale gas costs
  """
  total_sale_gas_eth: str
  """
    Users total mint count
  """
  mint_count: str
  """
    Users average mint gas usage
  """
  average_mint_gas_eth: str
  """
    Users average mint gwei cost
  """
  average_mint_gwei: str
  """
    Users average max priority fee cost
  """
  average_mint_max_prio_fee: str
  """
    Total amount of ETH the user has sent
  """
  total_eth_sent: str
  """
    Total amount of ETH the user has recieved
  """
  total_eth_recieved: str
  """
    Total amount of transaction the user has sent
  """
  total_tx_sent_count: str
  """
    Total amount of transactions the user has recieved
  """
  total_tx_received_count: str
  """
    Total amount of ERC721 tokens the user has recieved
  """
  total_erc721_recieved: str
  """
    Total amount of ERC721 tokens the user has sent
  """
  total_erc721_sent: str

class BatchUserTradingStatistics():
  """
    Users address identifier.
  """
  originalRequest: str
  """
    Users trading statistics.
  """
  data: UserTradingStatistics

class Token():
  """
    Token contract address
  """
  contract: str
  """
    Token id
  """
  token_id: str

class UserTradingHistory():
  """
    Type of in event
  """
  in_type: str
  """
    In source of trade
  """
  in_source: str
  """
    ETH price of transaction in
  """
  in_price_eth: int
  """
    USD price of transaction in
  """
  in_price_usd: int
  """
    In date of transaction
  """
  in_date: str
  """
    In transaction hash
  """
  in_tx: str
  """
    In transaction sender
  """
  in_from: str
  """
   *
  """
  in_to: str
  """
    Token traded
  """
  token: Token;
  """
    Type of trade
  """
  out_type: str
  """
    Source of the trade
  """
  out_source: str
  """
    Trade amount in ETH
  """
  out_price_eth: int
  """
    Trade amount in USD
  """
  out_price_usd: int
  """
    Trade transaction
  """
  out_tx: str
  """
    Date of trade
  """
  out_date: str
  """
    Sender address
  """
  out_from: str
  """
    Reciepent address
  """
  out_to: str

class CollectionIntersection():
  """
    Contract address that intersect
  """
  contracts: list[str]

class OwnedMetadata():
  """
    Collection name
  """
  name: str
  """
    Collection symbol
  """
  symbol: str
  """
    Collection description
  """
  description: str
  """
    Collection contract address
  """
  contractAddress: str
  """
    Collection NSFW flag
  """
  is_nswf: bool
  """
    Collections verified flag (OpenSea ONLY)
  """
  verified: bool
  """
    Collections ERC token standard
  """
  ercType: str
  """
    Collections ISO creation date
  """
  createdDate: str
  """
    Contract socials
    @type():Socials
  """
  socials: Socials
  """
    Collection images
    @type():Images
  """
  images: Images
  """
    Collection fees
    @type():Fees
  """
  fees: Fees
  """
    Collection statistics
    @type():Statistics
  """
  stats: Statistics

class CollectionsOwned():
  """
    Collections contract address
  """
  collectionAddress: str
  """
    Amount of tokens owned
  """
  tokensOwned: int
  """
    Token metadata
  """
  metadata: Metadata

class TransfersIn():
  """
    Transaction hash
  """
  txHash: str

class TokensOwnedMetadata():
  """
    Token nane
  """
  name: str
  """
    Token image
  """
  image: str
  """
    Token attribute
  """
  attributes: list[Attributes]
  """
    Token description
  """
  description: str

class TokensOwned():
  """
    Token id
  """
  tokenID: str
  """
    Token contract address
  """
  contractAddress: str
  """
    Token ERC type
  """
  type: str
  """
    Token transfers
  """
  transfersIn: list[TransfersIn]
  """
    Metadata of the token
  """
  metadata: TokensOwnedMetadata

class TokenOwner():
  """
    Token owner address
  """
  owner: str
  """
    The transaction hash of the relative token
  """
  transferTxhash: str

class Spread():
  """
    Number of tokens.
  """
  numTokens: int
  """
    Number of owners.
  """
  numOwners: int

class CollectionOwnerSpread():
  """
    Number of tokens.
  """
  numTokens: int
  """
    Number of owners.
  """
  numOwners: int

class MintVolume():
  totalMintVolume: int

class TokenInfo():
  collection: Optional[Collection]
  metadata: Optional[Metadata]
  listing: list[Listing]
  lastSale: Optional[Sale]
  owner: Optional[TokenOwner]

# METADATA
class Input():
  """
    Event name
  """
  name: str
  """
    Event type
  """
  type: str
  """
    Event internal type
  """
  internalType: str

class ABI():
  """
    Function name
  """
  name: str
  """
    Function type
  """
  type: str
  """
    Array of parameters
  """
  inputs: list[Input]
  """
    Functions state mutability state (read OR pure)
  """
  stateMutability: str
  """
    Functions anonymous field as declared in the contract
  """
  anonymous: str

class ContractABI():
  """
    Contract address associated with the ABI
  """
  contractAddress: str
  """
    Contracts ABI
  """
  abi: list[ABI]

class NFTMetadata():
  """
    Token unique address identifier
  """
  id: str
  """
    Tokens contract address
  """
  contract_address: str
  """
    Tokens unique id
  """
  token_id: str
  """
    Token metadata
  """
  metadata: Metadata


# CENTRAL
class CollectionResolved():
  address: str
  name: str
  data: Rankings

class Resolved():
  """
    Collections
  """
  collections: list[CollectionResolved]
