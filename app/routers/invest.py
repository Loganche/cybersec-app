from fastapi import APIRouter
from fastapi import Depends

from app.invest import get_accounts
from app.invest import get_info
from app.invest import get_user_tariff

router = APIRouter(
    prefix='/invest',
    tags=['invest'],
)


@router.get('/accounts')
async def get_accounts_call(accounts=Depends(get_accounts)):
    return accounts


@router.get('/info')
async def get_info_call(info=Depends(get_info)):
    return {'response': str(info)}


@router.get('/tariff')
async def get_user_tariff_call(tariff=Depends(get_user_tariff)):
    return {'response': str(tariff)}
