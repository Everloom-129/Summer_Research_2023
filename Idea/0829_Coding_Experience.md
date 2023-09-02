# 一些给ChatGPT编程的想法

## CLASS > JSON > TXT 

TXT 不是人写的格式，这东西太难Parse了

JSON是原生于python的dict(或者相反？)，跨软件使用比较困难

面对对象编程，写个class效果最好，东西好管理，就是内存容易爆（盯）



## Grammar matters

说起来，我感觉跟prompt gpt反向push了我分析语法

因为今天在debug prompt时，发现有一个问题就是：我的字打错了以及我语法有问题

当然，伟大的GPT大人可以预测正确的话，就像“汉字的序顺不影响读阅”一样，

只是会降低他思考速度和正确率

倒是可以简单的让他帮忙改正啦...

## Debug log

除了print之外还可以

> explain more about using Python's logging module for more complex scenarios. role play as a computer science professor

Certainly! As your computer science professor, let me emphasize why logging is an important aspect of software development. Debugging by using `print` statements is akin to using stone tools in the age of high-tech machinery—it gets the job done, but not as efficiently or elegantly. 

In computer science, when we deal with increasingly complex systems, we need sophisticated ways to trace the flow of data, understand the states the system enters, and diagnose any issues. Python's built-in `logging` module offers just that—flexibility and insight into your code's behavior without cluttering the terminal or requiring you to remove debug lines for production.

Here's a quick rundown:

### Basic Setup

The most basic usage is incredibly simple. Just import the `logging` module and start logging:

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```

### Log Levels

Note the use of different logging levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`). These allow you to specify the severity of the messages you are logging, and you can configure the logging system to only show you messages of a certain severity or higher.

### Customization

The `logging` module is highly configurable. You can specify different behaviors for different loggers in your application (yes, you can have more than one logger). 

```python
# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('logfile.log')

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
```

This allows, for example, debug messages to be written to a debug log file, errors to be sent to an admin via email, and critical errors to be sent over SMS to a phone.

### Real-World Scenario

In a complex system like a machine learning pipeline, each stage could have its own logger. That way, if your pipeline crashes or produces unexpected results, you can check the logs and quickly identify which stage started behaving unexpectedly. Is it the data cleaning, the training, or perhaps the evaluation stage? A well-designed logging mechanism can tell you.

Would you like to know more about any specific aspect?