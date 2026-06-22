from pydantic import BaseModel

class ReportCreate(BaseModel):
    post_id: int
    reported_user_id: int
    reporter_user_id: int
    reason: str

class TrustDeductionRequest(BaseModel):
    points: int
    
class CommunityTimeoutRequest(BaseModel):
    hours: int