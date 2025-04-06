from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_users():
    """Get all users."""
    return {"users": [{"id": 1, "name": "Test User"}]}

@router.get("/{user_id}")
def get_user(user_id: int):
    """Get a specific user by ID."""
    # Mock user data, in a real app would be from database
    if user_id != 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    return {"id": user_id, "name": "Test User"} 