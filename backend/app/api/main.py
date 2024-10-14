from fastapi import APIRouter

from app.api.routes import items, login, users, utils
from app.api.routes import roles

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
# 添加一个路由主app下
api_router.include_router(roles.router, prefix="/roles", tags=["roles"])
