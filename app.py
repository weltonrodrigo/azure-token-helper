
import asyncio
import logging
from typing import Optional

import aiohttp
import azure.core.exceptions
import azure.identity.aio
from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware


import config

# logging.basicConfig(level=logging.INFO)
ll = logging.getLogger("app")
ll.setLevel(logging.INFO)

if config.TENANT_ID:
    ll.warn("Using authentication based on environment variables")

    credential = azure.identity.aio.ClientSecretCredential(
        tenant_id=config.TENANT_ID,
        client_id=config.CLIENT_ID,
        client_secret=config.CLIENT_SECRET
    )
else:
    ll.warn("Using authentication based on managed identities.")
    credential = azure.identity.aio.DefaultAzureCredential()

# Process cors permitted origins
if config.CORS_ORIGINS:
    LIST_CORS_ORIGINS = config.CORS_ORIGINS.split(",")
    ll.warn(f"Allowing origins {LIST_CORS_ORIGINS}")
else:
    LIST_CORS_ORIGINS = []  # empty list deny all origins
    ll.warn(f"No AZURE_TOKEN_HELPER_SCOPE_CORS_ORIGINS set. Denying all origins.")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=LIST_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
    )

app.add_middleware(GZipMiddleware)

@app.get("/{full_path:path}", response_class=PlainTextResponse)
async def do() -> str:
    try:
        async with credential:
            token = await credential.get_token(config.SCOPE)
            return token.token
    except azure.core.exceptions.AzureError as e:
        raise HTTPException(status_code=500, detail=e.message)
    except aiohttp.ClientError as e:
        raise HTTPException(status_code=500, details=e)
