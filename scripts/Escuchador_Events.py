from web3 import Web3
import json

alchemy_url = "https://eth-mainnet.g.alchemy.com/v2/19ftJ7kv7aQUPag2jbkEmqVno-dSN7c0"
infura_url = "https://mainnet.infura.io/v3/2cc1007b47a44600a95bf88abb0f9c43"
sepolia_url = "https://sepolia.infura.io/v3/2cc1007b47a44600a95bf88abb0f9c43"

# configuring conection to RCP
w3 = Web3(Web3.HTTPProvider(sepolia_url))

# Print if web3 is successfully connected
print(w3.is_connected())

# load contract as an object
# info=json.load(open('storage.json'))

# Adresses configuration after deploying
contract_address = "0x59Ed78F93A6F2dCc4400695C976dc8262538B604"

# contract instance - llamar al contrato
contract = w3.eth.contract(
    address=contract_address, abi=json.load(open("storage_abi.json"))
)


def escuchadoreventos(event):
    print(f"Evento recibido:")
    print(event["args"])


filtro_evento = contract.events.Deposited.create_filter(fromBlock="latest")

while True:
    for event in filtro_evento.get_new_entries():
        escuchadoreventos(event)
