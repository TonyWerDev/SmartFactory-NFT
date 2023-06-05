from brownie import accounts, config, WareHouseNFT
from scripts.CuentaWallet import get_account

# Token URI de la imagen del NFT (puede ser una URL o una representación base64 de la imagen)
token_URI = "https://ipfs.io/ipfs/QmXnvdLPRX5X3AANmoikXpMVHccFcBUNfS5XDtYFyCjA6w"

opensea_URL = "https://testnets.opensea.io/es/assets/goerli/{}/{}"

ETHScan_URL = "https://sepolia.etherscan.io/tx/{}"

# Dirección del destinatario del NFT
recipient_address = "0x7bAeCA6E5152a21ffFAC275AEC133366383321d7"

""" 
Agrega cuentas desde terminal -- {brownie account new <Name>} 
account=accounts.add(os.getenv("PRIVATE_KEY")) //import os
"""


# Función para desplegar contrato y consultar la PRIVATE_KEY desde config
def nftcreated():
    account = accounts.add(config["wallets"]["from_key"])
    nftcollect = WareHouseNFT.deploy({"from": account})
    print(f"Cuenta Origen;", account)
    print(f"Cuenta Destino;", recipient_address, "\n")

    tx_hash = nftcollect.createNFT(recipient_address, token_URI, {"from": account})
    tx_hash.wait(1)
    tokenId = nftcollect.getLastTokenId()
    print(f"Increible! Ve tu NFT en; {opensea_URL.format(nftcollect.address, tokenId)}")

    print(f"Consulta tu contrato Inteligente en;")


def main():
    nftcreated()
