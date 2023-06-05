// SPDX-License-Identifier: MIT

pragma solidity >=0.7.0 <0.9.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol"; //V4.9.0 ERC721
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract WareHouseNFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    //Constructor Ag1[Nombre del NFT] --> Ag2[Simbolo o sigla]
    constructor() ERC721("Corazon-Blochain", "CVerde") {}

    //Función para crear un nuevo NFT
    function createNFT(
        address recipient,
        string memory tokenURI
    ) public onlyOwner returns (uint256) {
        _tokenIds.increment();

        uint256 newTokenId = _tokenIds.current();
        _safeMint(recipient, newTokenId); //Ag1[A quien se le da el nuevo NFT] -- Ag2[]
        _setTokenURI(newTokenId, tokenURI); //Ag1[El numero de NFT generado] -- Ag2[El ID unico de NFT]
        return newTokenId;
    }

    function getLastTokenId() external view returns (uint256) {
        return _tokenIds.current();
    }
}
