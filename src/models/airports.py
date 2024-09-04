from sqlalchemy.orm import Mapped, mapped_column
from src.config.db import Base


class Airport(Base):
    __tablename__ = "airport_data"

    type: Mapped[str] = mapped_column(nullable=False)
    elevation: Mapped[int] = mapped_column()
    continent: Mapped[str] = mapped_column(nullable=False)
    country_code: Mapped[str] = mapped_column(primary_key=True, nullable=False)
    region: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column(nullable=False)
    iata_code: Mapped[str] = mapped_column()
    icao_code: Mapped[str] = mapped_column()
    city: Mapped[str] = mapped_column()
    latitude: Mapped[str] = mapped_column()
    longitude: Mapped[float] = mapped_column()
    iata_icao: Mapped[float] = mapped_column()
    country: Mapped[str] = mapped_column(nullable=False)
    timezone: Mapped[str] = mapped_column()
    city_code: Mapped[str] = mapped_column()
