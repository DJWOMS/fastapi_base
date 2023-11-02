from fastapi import Depends

from .auth.services.auth_service import is_admin


IsAdmin = Depends(is_admin) #Annotated[AuthService, Depends(is_admin)]
