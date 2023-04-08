from fastapi import FastAPI
from schemas import graphql_app

app = FastAPI()
app.include_router(graphql_app, prefix='/graphql')

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level='info')