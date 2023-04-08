from fastapi import FastAPI
from typing import Optional
from sqlmodel import (
    SQLModel, 
    Field,
    create_engine,
    select,
    Session
)

engine = create_engine('sqlite:///dbrest.db')

class Pessoa(SQLModel, table=True):
    
    __table_args__ = {'extend_existing': True}
    
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    idade: int
    

#Cria o banco de dados 
SQLModel.metadata.create_all(engine)


app = FastAPI()

@app.get("/")
def home():
    
    return {"msg": "Hello World"}

@app.get("/pessoa")
def get_pessoa():
    query = select(Pessoa)
    with Session(engine) as session:
        result = session.execute(query).scalars().all()
    
    return result

@app.get("/pessoa-nome")
def get_pessoa():   
    query = select(Pessoa.nome)
    
    with Session(engine) as session:
        result = session.execute(query).scalars().all()
    
    return result


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("rest:app", host="0.0.0.0", port=8000, reload=True, log_level='info')