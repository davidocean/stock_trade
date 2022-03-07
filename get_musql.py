import akshare as ak
import pandas as pd
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm_table import *
import time


def main():
    session = db_connect()

    symbols = ["106.BABA", "105.FB", "106.NIO", "105.PDD", "105.TSLA", "107.VBR", "105.LULU", "105.AAPL", "105.GOOGL",
               "105.BILI", "106.NABL", "107.SPY", "106.ZH"]
    for symbol in symbols:
        df = get_stock_usdata(symbol)
        result_list = list_instance(df)
        session.add_all(result_list)
        session.commit()
    session.close()


# 将数据结果 dateframe进行拆解，每一个数据都是一个实例
def list_instance(df):
    result_list = []
    for index, row in df.iterrows():
        temp = Stock_us(symbol=row["symbol"], timestamp=row["日期"] + " 23:59:59", opening=row["开盘"],
                        closing=row["收盘"],
                        highest=row["最高"], lowest=row["最低"], volume=row["成交量"], turnover=row["成交额"],
                        oscillation=row["振幅"], quote_change=row["涨跌幅"],
                        quote_change_price=row["涨跌额"], turnover_rate=row["换手率"])
        result_list.append(temp)

    return result_list


# 连接数据库  mysql
def db_connect():
    engine = create_engine('mysql+pymysql://root:admin123@dai.davidocean.cc:3306/stock_info')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session

    # i1 =Stock_us(timestamp="20220202",opening=12.1,closing=1.1,highest=3.2,lowest=44.4,volume=3,turnover=45.1,oscillation=4.1,quote_change=4.1,quote_change_price=412.1,turnover_rate=41.1)
    # seesion.add(i1)
    # seesion.commit()
    # seesion.close()

    # stock_us_hist_df = ak.stock_us_hist(symbol='105.MTP', period="daily", start_date="19700101", end_date="22220101",
    #                                     adjust="qfq")
    # stock_us_hist_df.to_sql("s1",con=engine,if_exists="append",index_label='id')


# 去akshare调取历史数据  只能按天
def get_stock_usdata(symbol_name):
    stock_us_hist_df = ak.stock_us_hist(symbol=symbol_name, period="daily", start_date="19700101", end_date="22220101",
                                        adjust="qfq")
    stock_us_hist_df["symbol"] = symbol_name
    return stock_us_hist_df


if __name__ == '__main__':
    t1 = time.time()
    main()
    t2 = time.time()
    t = t2 - t1
    print("spend time : " + str(t))
