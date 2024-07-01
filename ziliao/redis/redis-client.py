#!/bin/env  python
#Author: ZhangJie
import redis
import  time
pool = redis.ConnectionPool(host="127.0.0.1", port=6379,password="")
r = redis.Redis(connection_pool=pool)
for i in range(100):
    r.set("key%d" % i,"value%d" % i)
    #time.sleep(0.1)
    data=r.get("key%d" % i)
    data=data.decode("utf-8")
    print(data)
