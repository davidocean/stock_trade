# 背景介绍
有一天妹子跟我说她不能再亏了，她要逆袭成为股神。我说好。
然后她就鼓捣我弄一个量化交易平台，我说连最基本的股票知识都没有，做不了。

她说：“哼”。

然后我们就开启了股票量化交易平台。工作内容是：她研究量化交易的策略，我开发。她是产品经理，我是技术架构师+开发工程师+软件测试+算法实现。

我们都对这样的分工表示赞同。

2022年3月5号，是一个阳光灿烂的周末，我们就开始了。往后每个周末都要话一天以上的时候一起捣鼓这个量化交易系统。

# 架构说明
两台腾讯云服务器，分别是2核4G的轻量级应用服务器。
服务器A，跑mysql数据库。
服务器B，跑量化交易系统。

# 目前进展
## V0.01版本 -- 2022.03.07
实现功能：
1. 重点股票历史数据建库，按天为单位入了十多只股票，有苹果，特斯拉，Google这些大拿，也有哔哩哔哩和知乎这些弱点的。
数据结构参考标准股票数据记录，类似于开盘价，成交额等。
2.实时监控单只股票，每隔两小时读取一次信息并入库和邮件发送。
3.Mysql数据库建设完成，stock_info库作为核心库。

版本说明：
经过周末两天的开发，完成了建库和预警系统开发。
本来想对知乎股价进行实时监控，判断是否超过阈值然后进行报警。但是妹子没有算好阈值，那就索性进行数据分发即可。


# 填坑记录
## 云服务器默认关闭25端口
为了更好的发送预警邮件，我搭建了一个poste邮箱服务器，但在python里面的smtplib就是无法通过。后来进行查证，是因为所有的云服务器都停掉了25端口，说是为了自家的邮箱更好的使用而不被端口占用。如果想要使用云服务器的25端口，就要申请解封，但只对标准云服务器，也就是说我这便宜买来的轻量级应用服务器还不能解封。所以兜兜转转，搞了半天，我的邮箱服务器还不能用。本来想重建邮箱服务器，换了端口啥的，后来想着这不重要的事就别花时间，就直接用网易的了。 


