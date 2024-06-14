import fastapi
from fastapi import Depends
from sqlalchemy.orm import Session
from db.db_config import get_db1, get_db2
from db.session_handler import SessionHandler

# API Route Definitions
router = fastapi.APIRouter()

@router.get("/obtener_motivos")
def execute_query(db: Session = Depends(get_db1)):  
    session_handler = SessionHandler()
    sql = "SELECT * FROM motivo ORDER BY nombre_motivo"
    return session_handler.execute_sql(db, sql, "")
