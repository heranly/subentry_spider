# coding: utf-8
# 生成设备的device_type与device_brand
import redis
import random
import time
PORT = 6379
HOST = '127.0.0.1'
# redis node
#REDIS_NODE_001 = 'r-uf6afd5f21ab53b4.redis.rds.aliyuncs.com'
#REDIS_PASSWORD = 'Stzz11!!'
#REDIS_PORT = 6379
#REDIS_DB = 255
redis_cli = redis.StrictRedis(port=PORT, host=HOST, decode_responses=True)
REDIS_DOUYIN_SET_DEVICE_TYPE_BRAND = 'redis_douyin_set_device_type_brand'


# 删除原来的设备type与brand
def delete_redis_set_device_type_brand():
    # 获取原来set中的总数
    device_sum = redis_cli.scard(REDIS_DOUYIN_SET_DEVICE_TYPE_BRAND)
    print('device_type_brand总数:', device_sum)
    i = 1
    # 删除完
    while i < device_sum:
        ss = redis_cli.spop(REDIS_DOUYIN_SET_DEVICE_TYPE_BRAND)
        #print ss
        i += 1
    # 添加一些默认的设备信息，以防任务失败
    default_device_list = ['google Pixel 2;google',
                           'MI 6;Xiaomi',
                           'MI 5;Xiaomi',
                           'MI 4;Xiaomi',
                           'MI 5s Plus;Xiaomi',
                           'Redmi Note 4;Xiaomi',
                           'Lenovo K8 Note;lenovo',
                           'SM-G9350;samsung',
                           'SM-G930K;samsung',
                           'HUAWEI MLA-AL10;HUAWEI',
                           'ALP-AL00;HUAWEI',
                           'HUAWEI MLA-L12;HUAWEI',
                           'SM-G955F;samsung',
                           'HUAWEI MLA-AL10;HUAWEI',
                           'ZUK Z2151;ZUK',
                           'ZUK123;ZUK2',
                           'vivo X20A;vivo',
                           'vivo X9i;vivo',
                           'Mi Note 27;Xiaomi']
    for dd in default_device_list:
        already_add = redis_cli.sadd(REDIS_DOUYIN_SET_DEVICE_TYPE_BRAND, dd)
        #print 'default device is:', already_add


# 生成新的设备type与brand加入到redis的set中
def get_redis_set_device_type_brand():
    device_list = ['google Pixel 2{};google', 'MI 6{};Xiaomi', 'MI 5{};Xiaomi', 'MI 4{};Xiaomi', 'MI 5{}s Plus;Xiaomi',
                   'Redmi Note 4{};Xiaomi', 'Lenovo K8{} Note;lenovo', 'SM-G9{};samsung', 'SM-G9{}K;samsung',
                   'HUAWEI MLA-AL10{};HUAWEI', 'ALP-AL0{};HUAWEI', 'HUAWEI MLA-L12{};HUAWEI', 'SM-G9{}F;samsung',
                   'ZUK Z2{};ZUK', 'ZUK1{};ZUK2', 'vivo X20{}A;vivo', 'vivo X9{}i;vivo', 'Mi Note 2{};Xiaomi']
    str_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                    'V', 'W', 'X', 'Y', 'Z']
    i = 1
    while i < 10000:
        L = []
        for iii in range(3):
            str_A = random.choice(str_list)
            L.append(str_A)
        str_A_list = ''.join(L)
        device_t_b = random.choice(device_list)
        s = device_t_b.format(str_A_list + str(random.randint(1, 999)))
        i += 1
        add_device = redis_cli.sadd(REDIS_DOUYIN_SET_DEVICE_TYPE_BRAND, s)
        #print 'get new device:', s
    ss = redis_cli.scard(REDIS_DOUYIN_SET_DEVICE_TYPE_BRAND)
    ss3 = time.localtime()
    tt3 = time.strftime('%Y-%m-%d %H:%M:%S', ss3)
    print(tt3, '--device_type_brand总数:', ss)


if __name__ == '__main__':
    # 删除原设备信息
    delete_redis_set_device_type_brand()
    # 生成新的设备信息
    get_redis_set_device_type_brand()
