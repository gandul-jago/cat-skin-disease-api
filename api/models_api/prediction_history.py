from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Numeric
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy import BigInteger


class Base(DeclarativeBase):
    pass

class PredictionHistory(Base):
    __tablename__ = "prediction_history"



    id = Column(BigInteger, primary_key=True, autoincrement=True)
    image = Column(String)
    prediction = Column(String)
    confidence = Column(Numeric(5,2))
    created_at = Column(DateTime, server_default=func.now())

