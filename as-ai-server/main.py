from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="AlignSpace API")

@app.get("/")
async def root():
    return {"message": "AlignSpace API is running"}

@app.get("/health")
async def health():
    return JSONResponse(status_code=200, content={"status": "healthy"})

@app.get("/api/status")
async def status():
    return {"status": "ok", "service": "alignspace-api"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
