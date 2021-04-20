1、接口自动化采用的python+requests+unittest的框架
2、格式说明：
    config 配置文件：数据库连接配置、邮件配置、token的存放
    lib 存放文件处理相关的目录报错：构建用例、选择执行的用例、连接数据库、日志、邮件发送等
    package存放第三方包
    report 存放日志、html报告
    test_data 存放测试用例，主要通过excel（因为使用的openxl，excel仅支持xlsx格式的读取）
           用例规则：A、请求方式：get、post等，如果是查询数据则为sql。
                     B、获取参数规则：通过key-value的形式获取
                        例子：a接口返回{"data":{"id":1}}需要获取a接口id，下一个参数格式"${a的用例id：data["id"]}"
    test_case 存放用例的目录，base_case.text为用例生成模板，所有的用例都是通过文本生成。
    utils   存放数据存放的方法  如：断言、生成随机数、获取token、读写config文件、基础配置数据
    run.py  执行脚本文件
 3、注意点：
    a、用例添加只需在excel编写，规则参照已经编写的用例。
    b、切换运营方、登录账号等，在utils.settings.py文件修改
    c、修改数据库参数、发送邮件的信息，在config文件修改。
    d、编写excel用例时，参数通过json文件，满足json格式，至少能保证参数格式正确性。
    e、如果用例执行失败，可在report的logs文件、html报告中找到错误的信息。
    f、调试可在run.py后，生成的test_case的用例，取消请求和响应的注释，可打印请求和响应的参数。
    g、如果还不能解决，可致电：18884129577