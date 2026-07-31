from fastapi import APIRouter
from fastapi import APIRouter, HTTPException
from app.services.entry_service import EntryService
from app.models.entry import AuraEntry

router = APIRouter(prefix="/entries", tags=["entries"])

@router.get("/")
def get_entries():
    service = EntryService()
    return service.get_history()

@router.post("/")
def create_entry(entry: AuraEntry):
    service = EntryService()
    try:
        service.add_entry(entry)
        return {"msg": "Aura clocked bruh!","entry": entry}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{date}")
def update_entry(date: str):
    service = EntryService()
    return {"msg": f"Update ur entry for {date}"}

@router.delete("/{date}")
def delete_entry(date: str):
    service = EntryService()
    return {"msg": f"Delete ur entry for {date}"}