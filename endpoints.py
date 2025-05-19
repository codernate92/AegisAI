from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from ..deps import get_session
from ...models import IOC, Summary
from ...schemas import IOCOut, SummaryOut
from ...services.feeds import fetch_all_iocs
from ...services.summarizer import generate_summary
import datetime as dt
import asyncio

router = APIRouter()

@router.post("/ingest", response_model=int)
async def ingest(db: Session = Depends(get_session)):
    iocs = await fetch_all_iocs()
    count = 0
    for value, typ in iocs:
        ioc = IOC(value=value, ioc_type=typ, first_seen=dt.datetime.utcnow(), last_seen=dt.datetime.utcnow())
        db.add(ioc)
        count += 1
    db.commit()
    asyncio.create_task(_summarize(iocs, db))
    return count

async def _summarize(iocs, db):
    text = await generate_summary(iocs)
    summary = Summary(created_at=dt.datetime.utcnow(), content=text)
    db.add(summary)
    db.commit()

@router.get("/iocs/latest", response_model=list[IOCOut])
def latest_iocs(limit: int = 20, db: Session = Depends(get_session)):
    stmt = select(IOC).order_by(IOC.last_seen.desc()).limit(limit)
    return db.exec(stmt).all()

@router.get("/summaries", response_model=list[SummaryOut])
def summaries(limit: int = 10, db: Session = Depends(get_session)):
    stmt = select(Summary).order_by(Summary.created_at.desc()).limit(limit)
    return db.exec(stmt).all()
