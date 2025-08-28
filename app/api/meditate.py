from fastapi import APIRouter

router = APIRouter()

@router.get("/meditate")
def meditate():
    return {"instruction": "Breathe slowly and let go."}
