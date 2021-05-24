from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"msg": "Not found"}},
)

@router.post("/")
async def create_user(id: int, name: str):
    return {
        "msg": "success",
        "user": {
            "id": 3,
            "name": "alra"
        }
    }

@router.get("/")
async def read_all_user():
    return [
        {"id":1, "name":"lathif"},
        {"id":2, "name":"rasyid"}
    ]

@router.get("/{id}")
async def read_user(id: int):
    return {"id":id, "name":"lathif"}

@router.put("/{id}")
async def update_user(id: int, name: str):
    return {"id":id, "name":name}
