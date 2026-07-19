"""Centralized error handling and standardized error responses."""

from fastapi import HTTPException, status
from enum import Enum
from typing import Optional


class ErrorCode(str, Enum):
    """Standard error codes for API responses."""
    VALIDATION_ERROR = "VALIDATION_ERROR"
    AUTHENTICATION_ERROR = "AUTHENTICATION_ERROR"
    AUTHORIZATION_ERROR = "AUTHORIZATION_ERROR"
    NOT_FOUND = "NOT_FOUND"
    CONFLICT = "CONFLICT"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    BUSINESS_LOGIC_ERROR = "BUSINESS_LOGIC_ERROR"


def raise_validation_error(detail: str, code: str = ErrorCode.VALIDATION_ERROR):
    """Raise a standardized validation error."""
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={
            "error": code,
            "message": detail
        }
    )


def raise_auth_error(detail: str = "Invalid credentials"):
    """Raise a standardized authentication error."""
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={
            "error": ErrorCode.AUTHENTICATION_ERROR,
            "message": detail
        },
        headers={"WWW-Authenticate": "Bearer"}
    )


def raise_forbidden_error(detail: str = "Insufficient permissions"):
    """Raise a standardized authorization error."""
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail={
            "error": ErrorCode.AUTHORIZATION_ERROR,
            "message": detail
        }
    )


def raise_not_found_error(detail: str = "Resource not found"):
    """Raise a standardized not found error."""
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={
            "error": ErrorCode.NOT_FOUND,
            "message": detail
        }
    )


def raise_conflict_error(detail: str):
    """Raise a standardized conflict error."""
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail={
            "error": ErrorCode.CONFLICT,
            "message": detail
        }
    )


def raise_business_logic_error(detail: str):
    """Raise an error for business logic violations."""
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail={
            "error": ErrorCode.BUSINESS_LOGIC_ERROR,
            "message": detail
        }
    )


def raise_internal_error(detail: str = "Internal server error"):
    """Raise a standardized internal server error."""
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail={
            "error": ErrorCode.INTERNAL_ERROR,
            "message": detail
        }
    )
