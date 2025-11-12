from sqlalchemy import Column, Integer, String
from core.core.DATABASE.base_class import Base


class Endereco(Base):
    __tablename__ = "enderecos"

    id = Column(Integer, primary_key=True, index=True)
    endereco = Column(String(255), nullable=False)
    cep = Column(String(10), nullable=False)