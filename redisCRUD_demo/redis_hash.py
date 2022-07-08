from redis import StrictRedis

if __name__ == '__main__':
    try:
        # 连接数据库
        # st = StrictRedis(host="localhost",port = 6379,db = 0) #默认
        st = StrictRedis()

        #添加/修改
        res = st.hset('User','zhangsan',2) #返回一个boolean值
        # print(res)

        #获取
        value = st.hget('User','zhangsan')
        print(value)

        #删除键名及其值
        # res = st.delete('User','zhangsan')
        # print(res)

        # 从键为name的散列表中获取所有映射键值对
        res = st.hgetall('User')
        print(res)

        # 获取所有健
        # res = st.keys()
        # print(res)
    except Exception as e:
        print(e)