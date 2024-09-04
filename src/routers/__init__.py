import fastapi
from src.routers.partner_iq import router as partner_iq_router

router = fastapi.APIRouter()


router.include_router(router=partner_iq_router)
