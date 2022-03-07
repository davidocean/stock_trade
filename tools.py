from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from orm_table import *
import akshare as ak
import pandas as pd
from datetime import datetime, timezone, timedelta


# 获取北京时间的日期 20220202 格式
def get_datestr():
    beijing_timezone = timezone(timedelta(hours=8))
    date_now = datetime.utcnow().astimezone(beijing_timezone).strftime("%Y%m%d")
    return date_now


# 获取最新价格
def get_stockdata(date_str, stock_num):
    stock_us_hist_min_em_df = ak.stock_us_hist_min_em(symbol=stock_num, start_date=date_str, end_date="22220101")
    if stock_us_hist_min_em_df.empty:  # 当日无数据，则为休息日，返回False
        return False
    stock_us_hist_min_em_df["symbol"] = stock_num
    lastone = stock_us_hist_min_em_df.iloc[-1]

    # return lastone  # 返回 最新的行

    return lastone.to_dict()# 返回字典 字段为：['时间', '开盘', '收盘', '最高', '最低', '成交量', '成交额', '最新价']


def post2db(last_row):
    engine = create_engine('mysql+pymysql://root:admin123@dai.davidocean.cc:3306/stock_info')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    pastemp = Stock_us_em(symbol=last_row["symbol"], timestamp=last_row["时间"], opening=last_row["开盘"],
                          closing=last_row["收盘"],
                          highest=last_row["最高"], lowest=last_row["最低"], volume=last_row["成交量"], turnover=last_row["成交额"],
                          last_price=last_row["最新价"])
    session.add(pastemp)
    session.commit()
    session.close()


if __name__ == '__main__':
    date_str = get_datestr()
    stock_num = "106.ZH"
    result = get_stockdata(date_str, stock_num)
    print(result)
