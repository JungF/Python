
import time
#获取当前时间,并且可以将时间戳转成时间元祖，gmtime是国际标准时间，localtime是当前时间
#时间元组
time.localtime([second])
time.gmtime([second])
#time.struct_time(tm_year=2019, tm_mon=12, tm_mday=27, tm_hour=11, tm_min=5, tm_sec=38, tm_wday=4, tm_yday=361, tm_isdst=0)

#返回当前时间字符串
time.asctime([时间元组]) #可以接收一个时间元组
time.ctime([seconde])  #可以接收一个时间戳
#'Fri Dec 27 11:06:53 2019'


#获取当前时间的时间戳
time.time() #返回国际标准时间戳
time.mktime(时间元组) #返回时间元组的时间戳

#延时或者等待
time.sleep(second)
