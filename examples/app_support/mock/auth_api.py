async def auth_api_mock(token: str) -> dict | None:
    if token == '12345':
        return {"id": 1, "permission": "admin"}
