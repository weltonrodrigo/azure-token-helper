# Azure token helper

Ever wanted to understand Azure authentication? Me too.

To use Azure Maps without letting your key in text plain inside your code, you'll
need to provide your single page application with a token to access maps API.

You'll need a token helper. This is it.

Environment variables:

```shell
AZURE_TENANT_ID=e8f5849e-5b15-4c2f-b4f3-0386b614971f
AZURE_CLIENT_ID=b51c2235-cff0-4f69-8dee-0f43c2ab4457
AZURE_CLIENT_SECRET=zoquIWM-vnX9kg_F~.kP38gpSB2B772eop

# List of allowed Origins
AZURE_TOKEN_HELPER_ALLOWED_CORS_ORIGINS=http://localhost:8001,https://cdpn.io
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
