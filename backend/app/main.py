from fastapi import FastAPI

from app.database.database import Base
from app.database.database import engine
from app.routers.college import router as college_router
from app.routers.user import router as user_router
from app.routers.auth import router as auth_router
from app.routers.block import router as block_router
from app.routers.stall import router as stall_router
from app.routers.menu_item import router as menu_item_router
from app.routers.cart import router as cart_router
from app.routers.order import router as order_router
from app.routers.event import router as event_router
from app.routers.post import router as post_router
from app.routers.comment import router as comment_router
from app.routers.vote import router as vote_router
from app.routers.report import router as report_router
from app.models.notification import Notification
from app.routers.notification import router as notification_router
from app.models.lost_found import LostFound
from app.routers.lost_found import router as lost_found_router
from app.models.marketplace_item import MarketplaceItem
from app.routers.marketplace import router as marketplace_router
from app.models.favorite import Favorite
from app.routers.favorite import router as favorite_router
from app.routers.admin import router as admin_router
from fastapi.middleware.cors import CORSMiddleware
from app.models import *


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CampusFlow API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(college_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(block_router)
app.include_router(stall_router)
app.include_router(menu_item_router)
app.include_router(cart_router)
app.include_router(order_router)
app.include_router(event_router)
app.include_router(post_router)
app.include_router(comment_router)
app.include_router(vote_router)
app.include_router(report_router)
app.include_router(notification_router)
app.include_router(lost_found_router)
app.include_router(marketplace_router)
app.include_router(favorite_router)
app.include_router(admin_router)

@app.get("/")
def root():
    return {
        "message": "CampusFlow Backend Running"
    }
