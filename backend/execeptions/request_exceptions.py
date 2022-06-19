from fastapi import HTTPException
from sqlalchemy.exc import *
from util.file_readers.yaml_reader import yamlReader
import os,sys
config=yamlReader(os.path.dirname(os.path.realpath(__file__)) + '/../constants/error_messages.yaml')
async def db_exceptions(e):
    if type(e).__name__==DatabaseError:
        raise HTTPException(status_code=404, detail=configParams.DatabaseError)
    elif type(e).__name__==InternalError:
        raise HTTPException(status_code=503, detail=configParams.InternalError)
    elif type(e).__name__==NotSupportedError:
        raise HTTPException(status_code=403, detail=configParams.NotSupportedError)
    elif type(e).__name__==SQLAlchemyError:
        raise HTTPException(status_code=403, detail=configParams.sqlAlchemyError)
    elif type(e).__name__==NoSuchTableError:
        raise HTTPException(status_code=404, detail=configParams.NoSuchTableError)
    elif type(e).__name__==DataError:
        raise HTTPException(status_code=400, detail=configParams.DataError)
    elif type(e).__name__==IntegrityError:
        raise HTTPException(status_code=400, detail=configParams.DataError)
    elif type(e).__name__==ImportError:
        raise HTTPException(status_code=500, detail=e)
