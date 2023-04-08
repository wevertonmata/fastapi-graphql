from models import Pessoa, Livro, engine
from sqlmodel import Session, select
from sqlalchemy.orm import joinedload

def post_pessoas(idade: int, nome: str):
    person = Pessoa(nome=nome, idade=idade)

    with Session(engine) as session:
        session.add(person)
        session.commit()
        session.refresh(person)

    return person

def get_pessoas(id: int = None, idade: int = None, limit: int = 3):
    
    query = select(Pessoa)
    
    if id:
        query = query.where(Pessoa.id == id) 
        
    if idade:
        query = query.where(Pessoa.idade == idade)    
    
    if limit:
        query = query.limit(limit)       
    
    with Session(engine) as session:
        result = session.execute(query).scalars().all()
    
    return result

def post_livros(titulo: str, pessoa_id: int):   
    livros = Livro(titulo=titulo, pessoa_id=pessoa_id)

    with Session(engine) as session:
        session.add(livros)
        session.commit()
        session.refresh(livros)

    return livros

def get_livros(self):
        query = select(Livro).options(joinedload('*'))
        with Session(engine) as session:
            result = session.execute(query).scalars().unique().all()

        return result