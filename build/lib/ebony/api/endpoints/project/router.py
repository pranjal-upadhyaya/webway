from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("/")
def get_projects():
    """Get all projects."""
    return {"projects": [{"id": 1, "name": "Test Project", "description": "A test project"}]}

@router.get("/{project_id}")
def get_project(project_id: int):
    """Get a specific project by ID."""
    # Mock project data, in a real app would be from database
    if project_id != 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with ID {project_id} not found"
        )
    return {"id": project_id, "name": "Test Project", "description": "A test project"} 