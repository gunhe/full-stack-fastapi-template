from fastapi import APIRouter, HTTPException
router = APIRouter()


@router.get("/")
def read_roles():
    """
    返回多个对象
    """
    return {"data": [], "count": 1}


@router.get("/{id}")
def read_role():
    """
    获取一个对象
    """
    return {"data": "read_role"}


def create_role():
    """
    新建一个对象
    """
    return {"data": "create_role"}


@router.put("/{id}")
def update_role():
    """
    修改一个对象
    """
    return {"data": "update_role"}


@router.delete("/{id}")
def delete_role():
    """
    删除一个对象
    """
    return {"data": "delete_role"}
