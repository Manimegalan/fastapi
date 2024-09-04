from sqlalchemy import select

from src.crud.base import BaseCRUDRepository

from src.models.airports import Airport


class PartnerIqCRUD(BaseCRUDRepository):
    async def list_partner(self):
        stmt = select(Airport.name, Airport.country_code).limit(1)
        query = await self.async_session.execute(statement=stmt)
        return query.mappings().all()
