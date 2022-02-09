from cmath import cos
import os

DEFAULT_SCOPE = "https://atlas.microsoft.com/.default"  # Azure maps

# Those are used by azure sdk
TENANT_ID = os.environ.get("AZURE_TENANT_ID")
CLIENT_ID = os.environ.get("AZURE_CLIENT_ID")
CLIENT_SECRET = os.environ.get("AZURE_CLIENT_SECRET")

# This is used by this app
SCOPE = os.environ.get("AZURE_TOKEN_HELPER_SCOPE", DEFAULT_SCOPE)
CORS_ORIGINS = os.environ.get("AZURE_TOKEN_HELPER_SCOPE_CORS_ORIGINS")
