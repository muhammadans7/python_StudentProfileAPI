from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        return Response({
            "error": "Internal Server Error",
            "detail": str(exc)  # remove str(exc) in production if you don’t want to leak info
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
