import json
from fastapi import APIRouter, Request, Depends

from src.dependencies import get_repo
from src.crud.PartnerIq import PartnerIqCRUD
from src.utils.response_handler import CustomResponse


router = APIRouter(prefix="", tags=["Partner IQ"])


@router.get(path="/list/partner", name="list_partner")
async def list_partner(
    partner_repo: PartnerIqCRUD = Depends(get_repo(PartnerIqCRUD))
):
    partner_list = await partner_repo.list_partner()
    return CustomResponse(partner_list)
