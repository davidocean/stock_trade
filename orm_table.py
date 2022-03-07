from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, DateTime, Float,String

Base = declarative_base()


class Stock_us(Base):
    __tablename__ = "do_stock_us_hist"
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    timestamp = Column(DateTime)
    opening = Column(Float)
    closing = Column(Float)
    highest = Column(Float)
    lowest = Column(Float)
    volume = Column(Integer)
    turnover = Column(Float)
    oscillation = Column(Float)
    quote_change = Column(Float)
    quote_change_price = Column(Float)
    turnover_rate = Column(Float)


class Stock_us_em(Base):
    __tablename__ = "do_stock_us_hist_min_em"
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    timestamp = Column(DateTime)
    opening = Column(Float)
    closing = Column(Float)
    highest = Column(Float)
    lowest = Column(Float)
    volume = Column(Integer)
    turnover = Column(Float)
    last_price = Column(Float)

