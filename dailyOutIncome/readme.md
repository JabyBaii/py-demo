首先呢，这个项目年前有也计划过，就是设计一个简易的界面，通过它来记录每日的开销，并写入数据库，最后要查看时要分门别类用一条sql解决，主要是设计。

使用一个账单库，每个类别用一个表，用时间消费或者收入产生的时间做主键？

具体类别有：
    生活消费表（吃）
    穿搭购物表（用）
    固定支出（住、行）
    自我投资表
    收益表

表字段设计：

序号 交易日期 金额 类别代码 消费说明 支付方式 订单编号 创建日期 修改日期


--
类别代码：
    A: 生活
    B：聚餐
    C: 烟酒
    D：用品
    E：穿搭
    F: 房租
    G: 水费
    H：电费
    I：网费
    J：出行
    K: 投资
    L: 收入
```bash
DROP TABLE IF EXISTS trans_category;
CREATE TABLE "trans_category" (
	"id"	INTEGER,
	"code"	TEXT,
	"category"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
)
-- 插入数据
INSERT INTO trans_category (code, category) VALUES ('A', '生活');
INSERT INTO trans_category (code, category) VALUES ('B', '聚餐');
INSERT INTO trans_category (code, category) VALUES ('C', '烟酒');
INSERT INTO trans_category (code, category) VALUES ('D', '用品');
INSERT INTO trans_category (code, category) VALUES ('E', '穿搭');
INSERT INTO trans_category (code, category) VALUES ('F', '房租');
INSERT INTO trans_category (code, category) VALUES ('G', '水费');
INSERT INTO trans_category (code, category) VALUES ('H', '电费');
INSERT INTO trans_category (code, category) VALUES ('I', '网费');
INSERT INTO trans_category (code, category) VALUES ('J', '出行');
INSERT INTO trans_category (code, category) VALUES ('K', '投资');
INSERT INTO trans_category (code, category) VALUES ('L', '收入');

```

--
支付方式：
    1：微信
    2：支付宝
    3：现金
    4：京东白条
    5：交通银行信用卡
    6：农商行信用卡
    7：其他银行卡

```bash
CREATE TABLE "payment" (
	"id"  INTEGER PRIMARY KEY AUTOINCREMENT,
	"code"	INTEGER,
	"payment"	TEXT
)

INSERT INTO payment (code, payment) VALUES ('1', '1：微信');
INSERT INTO payment (code, payment) VALUES ('2', '2：支付宝');
INSERT INTO payment (code, payment) VALUES ('3', '3：现金');
INSERT INTO payment (code, payment) VALUES ('4', '4：京东白条');
INSERT INTO payment (code, payment) VALUES ('5', '5：交通银行信用卡');
INSERT INTO payment (code, payment) VALUES ('6', '6：农商行信用卡');
INSERT INTO payment (code, payment) VALUES ('7', '7：其他银行卡');
```

