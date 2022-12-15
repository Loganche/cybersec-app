import os

from fastapi import Depends
from tinkoff.invest import AsyncClient
from tinkoff.invest.constants import INVEST_GRPC_API
from tinkoff.invest.constants import INVEST_GRPC_API_SANDBOX

TOKEN = 'ABC'  # os.environ['TINKOFF_TOKEN_PROD_READONLY']
TOKEN_SANDBOX = 'ABC'  # os.environ['TINKOFF_TOKEN_SANDBOX']


async def get_accounts():
    async with AsyncClient(
        token=TOKEN,
        sandbox_token=TOKEN_SANDBOX,
        target=INVEST_GRPC_API_SANDBOX,
    ) as client:
        return await client.users.get_accounts()


async def get_info():
    async with AsyncClient(
        token=TOKEN,
        sandbox_token=TOKEN_SANDBOX,
        target=INVEST_GRPC_API_SANDBOX,
    ) as client:
        return await client.users.get_info()


async def get_user_tariff():
    async with AsyncClient(
        token=TOKEN,
        sandbox_token=TOKEN_SANDBOX,
        target=INVEST_GRPC_API_SANDBOX,
    ) as client:
        return await client.users.get_user_tariff()
