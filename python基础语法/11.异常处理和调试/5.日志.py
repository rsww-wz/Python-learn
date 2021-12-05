"""
日志
    如果你在代码中加入print语句来输出某些变量的值，就可以使用记日志的方式来调式代码
    日志消息将描述程序执行何时到达日志函数调用，并列出你指定任何变量的值
    缺失日志信息表明有一部分代码从未被执行

logging模块四大组件
    logging  日志器  提供了应用程序的接口
    Handler  处理器  通过1o9gex在不同位置输出日志
    Formator 格式器  决定日志以什么的样式显示
    Filter   过滤器  过滤哪些需要记录输出，哪些需要丢弃

日志语法
    导入logging库
    当python记录一个事件的日志时，会创建一个LogRecord对象，保存关于该事件的信息

    打印日志信息
        logging.debug()函数
            使用这个函数时，debug()函数将调用basicConfig(),打印一行信息
            这行信息的格式时我们在basicConfig()函数中指定的
            并且包括传递给debug()的消息

日志级别
    日志级别按重要性把消息分为5个级别
        DEBUG：logging.debug()    级别最低，通常只有在诊断细节的时候，才会关注这些消息
        INFO：logging.info()      用于记录程序中的一般性事件
        WARNING：logging.warming() 表示可能的问题，它不会阻止程序工作
        ERROR：logging.error()     用于记录错误，它导致程序做某事失败
        CRITCAL:logging.critical()  最高级别，它导致或者将导致程序完全停止

    日志的好处在于，你可以改变想看到的日志消息的优先级
    向basicConfig()函数传入logging.DEBUG作为level关键字参数，将显示日志级别最低的消息
    查看其他级别的的方法类似，向basicConfig()函数传入对应级别的函数名即可

禁用日志
    logging.disable():手工删除所有日志调用
    向logging.disable()传入一个日记级别，就会进制该级别以及更低级别的日志
    logging.disable(logging.CRITCAL)：禁用所有日志

将日志记录到文件
    logging.basicConfig()接受fileName关键字参数
    调用这个函数，日志会被保存到对应地址的文件中
    """