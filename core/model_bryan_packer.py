"""
Módulo para o modelo BryanPacker.

Este módulo contém a definição do modelo de dados BryanPacker.
"""
from datetime import datetime

from sqlalchemy import Column, Integer, DateTime

from core.core.DATABASE.base_class import Base


class BryanPacker(Base):
    """
    Modelo de dados para a tabela bryan_packer.
    
    Attributes:
        id (int): Identificador único do registro.
        created_at (datetime): Data e hora de criação do registro.
    """
    
    __tablename__ = "bryan_packer"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)