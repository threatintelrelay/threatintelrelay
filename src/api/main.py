from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "ThreatIntelRelay MCP server is up!"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}
