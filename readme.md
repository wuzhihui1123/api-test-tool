### 
api-test-tool
===============

这是xyz的测试框架，用于http接口自动化测试

使用步骤
-------------
1. case目录下编写单元测试用例脚本，如
```
case/
├── bf_bankCard.py
├── bf_payment.py
└── bf_receipt.py
```

2. 在需要执行测试的函数上添加注解 @TestCase
``` python
@TestCase
def test_receipt():
    database.clear_table()
    result = http_util.post("/route/receipt/single", body=req_model.addreceiptparame("s001201711142226420"))
    assert_util.verify(result, state="0", resultCode="2001", resultMsg=u'等待收款', chnId="ch001")
```
3. 通过main入口执行单元测试
```
python main/main.py

```

使用规范
-------------
- 所有的测试用例都必须放在case这个目录下（注：不能在case的子目录下）
- @TestCase注解的函数不能有参数
