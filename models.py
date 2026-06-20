from datetime import datetime

from sqlalchemy import DateTime, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from config import get_connection_string


class Base(DeclarativeBase):
    pass


class VanurRecord(Base):
    __tablename__ = "vanur_records"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    part_number: Mapped[str] = mapped_column(String(100), nullable=False)
    blo_name: Mapped[str] = mapped_column(String(200), nullable=False)
    blo_designation: Mapped[str] = mapped_column(String(200), nullable=False)
    blo_mobile: Mapped[str] = mapped_column(String(20), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


engine = create_engine(get_connection_string(), echo=False)
SessionLocal = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(engine)
