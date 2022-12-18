pragma solidity ^0.6.0;

contract GasFeeContract {
    uint256 constant GAS_FEE = 1e18;


    uint256 public gasFeesCollected;

    function someFunction() public {

        require(msg.gas >= GAS_FEE, "Not enough gas provided to cover the fee.");


        msg.gas -= GAS_FEE;


        gasFeesCollected += GAS_FEE;

    }
}