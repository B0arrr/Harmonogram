from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def main_view():
    return {"name": "Jacek"}


@router.get("/get")
def get():
    return "adasd"
