import uuid
from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app import models, schemas, database, auth
from app.schemas import IssueCreate, IssueUpdate, IssueOut, IssueStatus
from app.auth import get_current_active_user

router = APIRouter(prefix="/api/v1/issues", tags=["issues"])

@router.get("/", response_model=list[IssueOut])
def get_issues(
    current_user: Annotated[schemas.User, Depends(get_current_active_user)],
    db: Session = Depends(database.get_db)
):
    """Retrieve all issues from the database."""
    return db.query(models.Issue).all()
 

@router.post("/", response_model=IssueOut, status_code=status.HTTP_201_CREATED)
def create_issue(
    payload: IssueCreate,
    current_user: Annotated[schemas.User, Depends(get_current_active_user)],
    db: Session = Depends(database.get_db)
):
    """Create a new issue in the persistent database."""
    new_issue = models.Issue(
        id=str(uuid.uuid4()),
        title=payload.title,
        description=payload.description,
        priority=payload.priority,
        status=IssueStatus.open,
    )
    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)
    return new_issue

@router.get("/{issue_id}", response_model=IssueOut)
def get_issue(
    issue_id: str,
    current_user: Annotated[schemas.User, Depends(get_current_active_user)],
    db: Session = Depends(database.get_db)
):
    """Retrieve a specific issue by ID from the database."""
    issue = db.query(models.Issue).filter(models.Issue.id == issue_id).first()
    if not issue:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
    return issue


@router.put("/{issue_id}", response_model=IssueOut)
def update_issue(
    issue_id: str, 
    payload: IssueUpdate,
    current_user: Annotated[schemas.User, Depends(get_current_active_user)],
    db: Session = Depends(database.get_db)
):
    """Update an existing issue in the database."""
    db_issue = db.query(models.Issue).filter(models.Issue.id == issue_id).first()
    if not db_issue:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
    
    # Update fields only if they are provided in the payload
    update_data = payload.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_issue, key, value)
    
    db.commit()
    db.refresh(db_issue)
    return db_issue


@router.delete("/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_issue(
    issue_id: str,
    current_user: Annotated[schemas.User, Depends(get_current_active_user)],
    db: Session = Depends(database.get_db)
):
    """Delete an issue by ID from the database."""
    db_issue = db.query(models.Issue).filter(models.Issue.id == issue_id).first()
    if not db_issue:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
    
    db.delete(db_issue)
    db.commit()
    return