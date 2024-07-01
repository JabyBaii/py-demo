#!/bin/bash
#Author: ZhangJie
NUM=`seq 1 100000`
for i in ${NUM};do
  redis-cli -h 127.0.0.1 set key-${i} value-${i}
  echo "key-${i} value-${i} 写入完成"
done
echo "十万个key写入到Redis完成"
