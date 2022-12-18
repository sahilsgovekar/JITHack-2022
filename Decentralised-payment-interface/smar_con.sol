pragma solidity ^0.6.0;

contract DigitalAsset {
    address public owner;
    uint256 public value;

    constructor() public {
        owner = msg.sender;
        value = 1e18; // Initialize the value to 1 ether
    }

    function sell(address _buyer) public {
        require(msg.sender == owner, "Only the owner can sell the asset.");
        require(_buyer != address(0), "Invalid buyer address.");

        owner = _buyer;
        _buyer.transfer(value);
    }
}