from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.report import Report
from app.models.user import User
from app.models.post import Post

from app.schemas.report import ReportCreate
from app.schemas.report import TrustDeductionRequest
from app.models.notification import Notification

from datetime import datetime
from datetime import timedelta

from app.schemas.report import CommunityTimeoutRequest

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.post("/")
def create_report(
    report: ReportCreate,
    db: Session = Depends(get_db)
):
    reported_user = (
        db.query(User)
        .filter(User.id == report.reported_user_id)
        .first()
    )

    reporter_user = (
        db.query(User)
        .filter(User.id == report.reporter_user_id)
        .first()
    )

    post = (
        db.query(Post)
        .filter(Post.id == report.post_id)
        .first()
    )

    if not reported_user:
        raise HTTPException(
            status_code=404,
            detail="Reported user not found"
        )

    if not reporter_user:
        raise HTTPException(
            status_code=404,
            detail="Reporter user not found"
        )

    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    new_report = Report(
        post_id=report.post_id,
        reported_user_id=report.reported_user_id,
        reporter_user_id=report.reporter_user_id,
        reason=report.reason
    )

    db.add(new_report)

    db.commit()

    db.refresh(new_report)

    return new_report


@router.get("/")
def get_reports(
    db: Session = Depends(get_db)
):
    return db.query(Report).all()

@router.get("/pending")
def get_pending_reports(
    db: Session = Depends(get_db)
):
    return (
        db.query(Report)
        .filter(
            Report.status == "PENDING"
        )
        .all()
    )

@router.post("/{report_id}/approve")
def approve_report(
    report_id: int,
    db: Session = Depends(get_db)
):
    report = (
        db.query(Report)
        .filter(
            Report.id == report_id
        )
        .first()
    )

    if not report:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    report.status = "APPROVED"
    
    db.add(
    Notification(
        user_id=report.reported_user_id,
        message="A report against your content was approved."
    )
)

    db.commit()

    return {
        "message": "Report approved"
    }

@router.post("/{report_id}/reject")
def reject_report(
    report_id: int,
    db: Session = Depends(get_db)
):
    report = (
        db.query(Report)
        .filter(
            Report.id == report_id
        )
        .first()
    )

    if not report:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    report.status = "REJECTED"
    
    db.add(
    Notification(
        user_id=report.reporter_user_id,
        message="Your report was reviewed and rejected."
    )
)

    db.commit()

    return {
        "message": "Report rejected"
    }

@router.post("/{report_id}/trust-deduction")
def deduct_trust(
    report_id: int,
    request: TrustDeductionRequest,
    db: Session = Depends(get_db)
):
    report = (
        db.query(Report)
        .filter(Report.id == report_id)
        .first()
    )

    if not report:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    user = (
        db.query(User)
        .filter(
            User.id == report.reported_user_id
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.trust_score -= request.points

    if user.trust_score < 0:
        user.trust_score = 0

    db.commit()

    return {
        "user_id": user.id,
        "trust_score": user.trust_score
    }
    
    
@router.post("/{report_id}/community-timeout")
def community_timeout(
    report_id: int,
    request: CommunityTimeoutRequest,
    db: Session = Depends(get_db)
):
    report = (
        db.query(Report)
        .filter(Report.id == report_id)
        .first()
    )

    if not report:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    user = (
        db.query(User)
        .filter(
            User.id == report.reported_user_id
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.community_timeout_until = (
        datetime.utcnow()
        + timedelta(hours=request.hours)
    )

    db.commit()

    return {
        "user_id": user.id,
        "timeout_until": user.community_timeout_until
    }