# 通过pymongo驱动连接mongodb数据库

import pymongo

# 创建连接对象
client = pymongo.MongoClient('127.0.0.1', port=27017)

# 获取数据库, 如果没有该数据库它会自动创建一个
db = client.zhihu

# 获取数据库中的集合，也就是表
collection = db.qa

# 1、往数据库中写入数据
# collection.insert({'username': 'tom'})  # 插入一条数据
# collection.insert_many([
#     {
#         'username': 'jerry',
#         'age': 24
#     },
#     {
#         'title': 'xzxx',
#         'content': 'rrrrr'
#     },
#
# ])  # 插入多条数据


# 2、查找数据
# cursor = collection.find()  # 查找全部数据
# for x in cursor:
#     print(x)

# result = collection.find_one()  # 查找第一条数据
# print(result)
# result = collection.find_one({'age': 24})  # 根据条件查找数据
# print(result)


# 3、更新数据
# collection.update_one({'username': 'tom'}, {'$set': {'username': 'jerry'}})  # 根据条件更新一条数据
# collection.update_many({'username': 'jerry'}, {'$set': {'username': 'tom'}})  # 根据条件更新多条数据


# 4、删除数据
# collection.delete_one({'title': 'uuu'})  # 根据条件删除一条数据
collection.delete_many({'username': 'tom'})  # 根据条件删除多条数据
