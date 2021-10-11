from brownie.network import account
from scripts.aave_borrow import get_asset_price, get_lending_pool, approve_erc20 
from brownie import config, network
from scripts.helpful_scripts import get_account

def test_get_asset_price():
    # arrange/act
    asset_price = get_asset_price(config["networks"][network.show_active()]["dai_eth_price_feed"])
    # assert
    assert asset_price > 0

def test_get_lending_pool():
    # arrange/act
    lending_pool = get_lending_pool()
    # assert
    assert lending_pool is not None

def test_approve_erc20():
    # arrange/act
    account = get_account()
    lending_pool = get_lending_pool()
    value = 1*10*17
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    tx = approve_erc20(lending_pool.address,value, erc20_address,account)
    # assert
    assert tx is not None