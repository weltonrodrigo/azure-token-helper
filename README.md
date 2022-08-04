# Azure token helper

## Synopsis

```console
foo@bar:~$ docker run --rm -ti -p 8080:80 \
   -e AZURE_TENANT_ID=e8f5849e-5b15-4c2f-b4f3-0386b614971f \
   -e AZURE_CLIENT_ID=b51c2235-cff0-4f69-8dee-0f43c2ab4457 \
   -e AZURE_CLIENT_SECRET=zoquIWM-vnX9kg_F~.kP38gpSB2B772eop \
   weltonrodrigo/azure-token-helper

Using authentication based on environment variables
No AZURE_TOKEN_HELPER_ALLOWED_CORS_ORIGINS set. Denying all origins.
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)
```
Now you can do a HTTP request for the token

```console
foo@bar:~$ curl -v localhost:8080/
eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjJaUXBKM1VwYmpBWVhZR235RUpsOGxWMFRPSSIsImtpZCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSJ9.eyJhdWQiOiJodHRwczovL2F0bGFzLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9lOGY1ODQ5ZS01YjE1LTRjMmYtYjRmMy0wMzg2YjYwNDk3MWUvIiwiaWF0IjoxNjU5NjQ0NzExLCJuYmYiOjE2NTk2NDQ3MTEsImV4cCI6MTY1OTY0ODYxMSwiYWlvIjoiRTJaZ1lKRGVlR2pYQXYxNW13STBEaG9sR1g5TEFBQT0iLCJhcHBpZCI6ImQ2ZTdmNjY3LTRlMTYtNGJkZS1iMThmLWJlNDRiZTFhMzJjMCIsImFwcGlkYWNyIjoiMSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0L2U4ZjU4NDllLTViMTUtNGMyZi1iNGYzLTAzODZiNjA0OTcxZS8iLCJvaWQiOiI1YzFhODdjNy1jZTM2LTRlZTktYTQxNy04MjkyNDE0ZmNjYjEiLCJyaCI6IjAuQVRRQW5vVDE2QlZiTDB5MDh3T0d0Z1NYSGlLZ0hyb0hXTlZCdS1zcExINGM5ZlkwQUFBLiIsInN1YiI6IjVjMWE4N2M3LWNlMzYtNGVlOS1hNDE3LTgyOTI0MTRmY2NiMSIsInRpZCI6ImU4ZjU4NDllLTViMTUtNGMyZi1iNGYzLTAzODZiNjA0OTcxZSIsInV0aSI6ImdPczJiYm1lWDBtWHRLUzBMdlk1QUEiLCJ2ZXIiOiIxLjAifQ.UfGgbXb2i9EyDYaMzvUlr1n9M56rIdL07j2CDue1rTRDQWOQukDOaD0HeDFYqrsYfc-Ev1uQCU__GxLw9KbvttArhgMYrIdQwyUjdv1iB0GMrYdfbHnk234rIyWtFZiA2JIcxD-fTPTsWu5CWJdy4nnBSUjM1_K869XjBOgvQhfJ5wFj5sFwhgwv8dknqgjB1R19F1pdkDPtMk-jkiIg6xw1HsM6bE6Dqq9lVoPRJAkJPrlE89V12pybNPArDg_Yqv4x-gZbeFwV1T1QTXb6qqYcx4f44U-egy41PpnlKtQJJIC50lu7xbTzeEBc2xX_16zGR9m669B80s316zaQnA
```
---

Ever wanted to understand Azure authentication? Me too.

To use Azure Maps without letting your key in text plain inside your code, you'll
need to provide your single page application with a token to access maps API.

You'll need a token helper. This is it.

Environment variables:

```shell
# Note that you still have to give this client permission
# to impersonate itself for the scope you want.
# This is done at Azure Active Directory App Registrations
AZURE_TENANT_ID=e8f5849e-5b15-4c2f-b4f3-0386b614971f
AZURE_CLIENT_ID=b51c2235-cff0-4f69-8dee-0f43c2ab4457
AZURE_CLIENT_SECRET=zoquIWM-vnX9kg_F~.kP38gpSB2B772eop

# List of allowed Origins
AZURE_TOKEN_HELPER_ALLOWED_CORS_ORIGINS=http://localhost:8001,https://cdpn.io

# Scope for the requested token
# Default is https://atlas.microsoft.com/.default , for Azure Maps,
# but you can actually use this for any azure scope, given proper
# permissions.
AZURE_TOKEN_HELPER_SCOPE=https://atlas.microsoft.com/.default
```

Open an issue if you need help creating the application credentials in Azure AD and I'll
document it here. Basically, you can use the script ```create_credentials.azcli```

You still will need to add permission to impersonate the user on the API and to query Azure Maps.

The first is done in Azure AD Application Registration, on API permission.

The later is on IAM of Azure Maps resource.

Good luck.

Help me improve this documentation.

[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)

Run this on google cloud run, it's so much easier LOL. You still need the credentials, tough.
