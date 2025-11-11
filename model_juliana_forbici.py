from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from core.core.DATABASE.base_class import Base


class JulianaForbici(Base):
    __tablename__ = "juliana_forbici"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    nome = Column(String(100))
    cep = Column(String(9))
    rua = Column(String(200))

    def __repr__(self) -> str:
        return f"<JulianaForbici(id={self.id}, nome={self.nome})>"
