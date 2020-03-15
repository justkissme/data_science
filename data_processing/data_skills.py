#strip() 去除首尾多余的空格
movie = '         你好啊        好   '
a=movie.strip()
print(a)

#replace()替换
movie = '   这是什么啊   怎么这么多空格   '
a = movie.replace(' ','')
print(a)

#split()将字符串通过参数分割,得到一个列表
movie = '2025/中国/天才科学家/刘洋洋'
a = movie.split('/')
print(a)

#url的拼接
list1 = ['hello','ahelloa','bhellob','chelloc']
for i in range(4):
    if not list1[i].startswith('he'):
        list1[i] = 'hello'+list1[i]
print(list1)

#剔除多余的url
list2 = ['hello.jpg','hello.pne','hello.pdf','nice.jpg']
for i in list2:
    if i.endswith('jpg'):
        list2.remove(i)
print(list2)

#拼接序列join()
tag = ['刘洋洋','是个','大','帅逼']
tag = '❥'.join(tag)
print(tag)

#列表的去重
content = ['cool','beautiful','nice','beautiful','nice']
new_content = set(content)#将列表转换成集合,集合内元素不能重复,但它是无序的
print(new_content)
new_content = list(new_content)#集合转化成列表
print(new_content)