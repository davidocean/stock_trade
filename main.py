import schedule
import time
from tools import *
from email_control import *


def job():
    date_str = get_datestr()
    stock_num = "106.ZH"  # 知乎代码
    lastone = get_stockdata(date_str, stock_num)
    if lastone != False:
        post2db(lastone)
        sendEmail(lastone)  # 发送邮件
    else:
        print("今日休市，不进行信息发送")
    print("I'm working...")


# 美股时间 9:30 - 16:00  非夏令时 --> 中国时间 22:30 - 5:00
#                       夏令时 --> 中国时间 21：30－4：00
for i in ["22:30", "00:30", "01:30", "03:30", "05:00"]:  # 周二到周五正常
    schedule.every().tuesday.at(i).do(job)
    schedule.every().wednesday.at(i).do(job)
    schedule.every().thursday.at(i).do(job)
    schedule.every().friday.at(i).do(job)
for j in ["00:30", "01:30", "03:30", "05:00"]:  # 周六特例
    schedule.every().saturday.at(j).do(job)

schedule.every().monday.at("22:30").do(job)  # 周一特例

# schedule.every().day_of_week.at("22:30").do(job)
# schedule.every().monday.at("22:30").do(job)
# schedule.every(2).hours.do(job)
# schedule.every().day.at("10:00").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)
# schedule.every(2).seconds.do(job)
# schedule.every(10).minutes.do(job)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
