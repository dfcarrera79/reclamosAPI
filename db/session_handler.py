from sqlalchemy import text
from sqlalchemy.orm import Session

class SessionHandler:
    def execute_sql(self, db: Session, sql: str, mensaje: str):
        try:
            with db.begin():
                rows = db.execute(text(sql)).fetchall()
                objetos = [row._asdict() for row in rows]
                return {"error": "N", "mensaje": mensaje, "objetos": objetos}
        except Exception as error:
            return {"error": "S", "mensaje": str(error), "objetos": ""}

    