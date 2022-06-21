from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from fastapi import FastAPI,Depends
from fastapi.exceptions import HTTPException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

def token_validation(token:str=Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        detail="invalid token",
        headers={"WWW-Authenticate": "Bearer"},
        status_code=401,
    )
    if token == "ABCDEFGH":
        return True
    else :
        raise credentials_exception