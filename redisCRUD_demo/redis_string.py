from redis import StrictRedis

if __name__ == '__main__':
    try:
        # 连接数据库
        # st = StrictRedis(host="localhost",port = 6379,db = 0) #默认
        st = StrictRedis()

        #添加/修改
        res = st.set('name','zhangsan') #返回一个boolean值
        # print(res)

        #获取
        value = st.get('name')
        # print(value)

        #删除key以及值，可删除多个，返回删除的数量
        # res = st.delete('name')
        # print(res)

        # 获取所有健
        res = st.keys()
        print(res)
    except Exception as e:
        print(e)