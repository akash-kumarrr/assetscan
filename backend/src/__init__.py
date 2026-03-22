from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from config.config import setting
from api import asset, auth
import uvicorn

app = FastAPI(
    title=setting.PROJECT_NAME,
    description=setting.PROJECT_DESCRIPTION,
    version=setting.VERSION,
    debug=setting.DEBUG
)

@app.on_event("startup")
async def start():
    print("System Initializing !!")
    return {
        "message" : "App-Backend is launched successfully !"
    }

@app.on_event("shutdown")
async def stop():
    print("System is shutting down!")
    return {
        "message" : "App is shut down successfully !"
    }


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=asset.router)
app.include_router(router=auth.router)

@app.get("/")
async def root():
    return {
        "message" : "This is backend of AssetScan",
        "version" : setting.VERSION,
        "description" : "AssetScan is a professional utility designed to bridge the gap between physical hardware and digital records using high-speed QR technology.",
        "docs"  : "/docs"
    }

@app.get("/api/info")
async def api_info():
    return {
        'name' : setting.PROJECT_NAME,
        'version' : setting.VERSION,
        'description' : setting.PROJECT_DESCRIPTION,
        'endpoins' : {
            'user' : '/api/users',
            'assets' : '/api/assets'
        }
    }

if __name__ == '__main__':
    uvicorn.run(app, host=setting.host, port=setting.port)