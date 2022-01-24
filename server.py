from fastapi import FastAPI
from jwt import ExpiredSignatureError, ImmatureSignatureError, InvalidAlgorithmError, InvalidAudienceError, \
    InvalidKeyError, InvalidSignatureError, InvalidTokenError, MissingRequiredClaimError
from starlette import status
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

from auth import decode_and_validate_token

server = FastAPI(debug=True)


class AuthorizeRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        if request.url.path in ["/docs", "/openapi.json"]:
            return await call_next(request)
        if request.method == "OPTIONS":
            return await call_next(request)

        bearer_token = request.headers.get("Authorization")
        if not bearer_token:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "detail": "Missing access token",
                    "body": "Missing access token",
                }
            )
        try:
            auth_token = bearer_token.split(" ")[1].strip()
            token_payload = decode_and_validate_token(auth_token)
        except (
                ExpiredSignatureError,
                ImmatureSignatureError,
                InvalidAlgorithmError,
                InvalidAudienceError,
                InvalidKeyError,
                InvalidSignatureError,
                InvalidTokenError,
                MissingRequiredClaimError,
        ) as error:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": str(error), "body": str(error)}
            )
        else:
            request.state.user_id = token_payload["sub"]
        return await call_next(request)


server.add_middleware(AuthorizeRequestMiddleware)


server.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

import api
