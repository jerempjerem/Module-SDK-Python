# Module Python SDK (Non official)

**Information 📖**

Some methods have names that differ from their api counterparts on the documentation as a result of consistency for the SDK.

**Features ✨**

Have a specific feature that you want added? Open a ticket in their discord and they can discuss building it for you!

**Feedback/Issues 🤝**

We welcome feedback and pull requests! Either open a ticket in they discord or open an issue on the repo and we can look into it!


# Getting Started
This module requires Python 3 or later. Python 3
```zsh
pip install module_sdk
```

After installing the SDK, import it using the following code
```python
from module_sdk import Module

api_key = 'Your api key' # Module API Key. Not required, however rate limits will apply.

# Create a new instance of the SDK
client = Module(api_key=api_key)
```

# SDK Usage

All methods are exposed through their own classes. 
There are four usable classes as shown below
```python
from module_sdk import Module
client = Module()

client.eth # Ethereum Methods
client.nft # NFT Methods
client.centra # Central Methods
client.metadata # Metadata Methods
```

# Method Documentation
Refer below for information on each classes methods.

- [NFT Methods](./docs/nft.md)
- [ETH Methods](./docs/eth.md)
- [Central Methods](./docs/central.md)
- [Metadata Methods](./docs/metadata.md)


# Examples
Getting azuki collection info
```python
from module_sdk import Module

client = Module()
collectionInfo = client.nft.getCollectionInfo({slug: 'azuki'})
```
Getting azuki contract abi
```python
from module_sdk import Module

client = Module()
abi = client.metadata.getContractABI({contractAddress:'0xed5af388653567af2f388e6224dc7c4b3241c544'})
```