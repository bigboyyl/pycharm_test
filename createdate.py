# coding=utf-8

#代码如下：

import random
import datetime
import time

dataCount = 10 * 100 * 100  # 10M.
codeRange = range(ord('a'), ord('z'))
alphaRange = [chr(x) for x in codeRange]
alphaMax = len(alphaRange)
daysMax = 42003
theDay = datetime.date(1900, 1, 1)

# 姓名随机
def genRandomName(nameLength):
    global alphaRange, alphaMax
    length = random.randint(1, nameLength)
    name = ''
    for i in range(length):
        name += alphaRange[random.randint(0, alphaMax - 1)]
    return name

# 生日随机
def genRandomDay():
    global daysMax, theDay
    mDays = random.randint(0, daysMax)
    mDate = theDay + datetime.timedelta(days=mDays)
    return mDate.isoformat()

# 性别随机
def genRandomSex():
    return random.randint(0, 1)


def genDataBase1(fileName, dataCount):
    outp = open(fileName, 'w')
    i = 0
    while i < dataCount:
        firstName = genRandomName(14)
        lastName = genRandomName(14)
        birthday = genRandomDay()
        sex = genRandomSex()
        mLine = "%i %s %s %s %d\n" % (i + 1, firstName, lastName, birthday, sex)
        outp.write(mLine)
        i += 1
        # 每次循环都把数据输入到磁盘
        outp.flush()
        time.sleep(2)
    # 如果没有调用flush函数，在调用write函数时，数据会先进入内存缓冲区
    # 当内存缓冲区满或者调用clost函数后数据才会写入磁盘
    outp.close()


if __name__ == "__main__":
    random.seed()
    start = time.time()
    genDataBase1('db_test.txt', dataCount)
    end = time.time()
    print('use time:%d' % (end - start))
    print('Ok')