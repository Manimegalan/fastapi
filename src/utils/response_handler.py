from fastapi import Request, status
from fastapi.responses import JSONResponse


class CustomException(Exception):
    def __init__(self, data, status_code, state=False):
        response = {"status": state, "status_code": status_code}
        if state:
            response["data"] = data
        else:
            if isinstance(data, str):
                response["error"] = {"message": data}
            else:
                response["error"] = data
        self.status_code = status_code
        self.response = response


async def CustomExceptionHandler(
    request: Request, exc: CustomException
) -> JSONResponse:
    return JSONResponse(exc.response, exc.status_code)


def CustomResponse(data, status_code=status.HTTP_200_OK, state=True):
    response = {"status": state, "status_code": status_code}
    if state:
        response["data"] = data
    else:
        if isinstance(data, str):
            response["error"] = {"message": data}
        else:
            response["error"] = data
    return response
