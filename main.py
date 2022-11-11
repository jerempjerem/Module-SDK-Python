from module_sdk import Module

client = Module()

r = client.eth.getFullTX({'txHash': '0x8cbd04383b405ae23659c7e506ae20cf925f6db17011232dd2e3ed2b31156e7b'})

print(r)