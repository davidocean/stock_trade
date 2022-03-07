import smtplib
import email
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header


def sendEmail(input_dict):
    # SMTP服务器,这里使用163邮箱
    mail_host = "smtp.davidocean.cc"
    # 发件人邮箱
    mail_sender = "david_ocean@163.com"
    # 邮箱授权码,注意这里不是邮箱密码,如何获取邮箱授权码,请看本文最后教程
    mail_license = "PZHZJAEGEKSQATWT"
    # 收件人邮箱，可以为多个收件人
    mail_receivers = ["2735403137@qq.com", "season1016@gmail.com"]
    mm = MIMEMultipart('related')
    # 邮件主题
    subject_content = "简报：知乎股票{}".format(input_dict["时间"])
    # 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱
    mm["From"] = "notice<david_ocean@163.com>"
    # 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱
    mm["To"] = "zhen<season1016@gmail.com>,dai<2735403137@qq.com>"
    # mm["To"] = "dai<2735403137@qq.com>"
    # 设置邮件主题
    mm["Subject"] = Header(subject_content, 'utf-8')

    # 邮件正文内容
    body_content = "你好，知乎股价情况实时播报\n"
    for key in input_dict:
        body_content = body_content + "{key} : {value} \n".format(key=key, value=input_dict[key])

    # 构造文本,参数1：正文内容，参数2：文本格式，参数3：编码方式
    message_text = MIMEText(body_content, "plain", "utf-8")
    # 向MIMEMultipart对象中添加文本对象
    mm.attach(message_text)

    # 创建SMTP对象
    # smtpObj = smtplib.SMTP("smtp.davidocean.cc", 465)
    smtpObj = smtplib.SMTP("smtp.163.com", 25)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.ehlo()
    smtpObj.login(mail_sender, mail_license)
    # 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
    smtpObj.sendmail(mail_sender, mail_receivers, mm.as_string())
    print("邮件发送成功")
    # 关闭SMTP对象
    smtpObj.quit()


if __name__ == '__main__':
    sendEmail()
