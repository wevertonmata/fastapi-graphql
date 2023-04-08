from typing import Optional, List
from sqlmodel import (
    SQLModel,
    Field,
    create_engine,
    Relationship
)

# Criar engine do banco
engine = create_engine('sqlite:///database.db')


class Pessoa(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    idade: int
    
    livro: List["Livro"] = Relationship(back_populates='pessoa')
    
class Livro(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    
    pessoa_id: Optional[int] = Field(default=None, foreign_key='pessoa.id') 
    pessoa: Optional[Pessoa] = Relationship(back_populates='livro')

# Cria o banco de dados
SQLModel.metadata.create_all(engine)