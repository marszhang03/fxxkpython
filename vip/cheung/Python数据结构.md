
# 列表 list

列表可以用list()函数表示，也可以使用中括号（[]）表示。

列表的一般操作有删、增、改和查。



```python
# 列表的表示
songs = ['像我这样的人','光','孤独之书','艺术家','水星记','飞','流年','红豆','100种生活',
        '残缺的彩虹','毒苹果','当冬夜渐凉','脆弱的一分钟','我真的受伤了']
```

---
### 查


```python
#查询单个列表
songs[0]
```




    '像我这样的人'




```python
#查询一段列表
songs[1:5]
```




    ['光', '孤独之书', '艺术家', '水星记']




```python
#由后往前查
songs[-3]
```




    '当冬夜渐凉'




```python
#查询从某个元素往后的所有元素
songs[2:]
```




    ['孤独之书',
     '艺术家',
     '水星记',
     '飞',
     '流年',
     '红豆',
     '100种生活',
     '残缺的彩虹',
     '毒苹果',
     '当冬夜渐凉',
     '脆弱的一分钟',
     '我真的受伤了']



---
### 改


```python
#直接查到某个元素，然后直接赋值
songs[2] = '曹操'
```


```python
songs[2]
```




    '曹操'



---
### 删
一种是使用del；一种是调用remove()方法。

del需要知道列表的下标；而remove方法需要知道元素名称。


```python
del songs[2]
```


```python
songs[2]
```




    '艺术家'




```python
songs.remove('毒苹果')
```

---
### 增
一种是insert方法；一种是append()方法。

insert方法可以指定增加的元素位置；而append方法往往是在列表末尾增加。


```python
songs.insert(2,'亲爱的')
```


```python
songs[2]
```




    '亲爱的'




```python
songs.append('童年')
```


```python
songs[-1]
```




    '童年'



---
### list常用到的操作
1. len() ，查看列表的长度
2. index() ，查看某个元素的索引
3. reverse()，反向安排元素
4. pop()，移除列表中的一个元素（默认最后一个）并返回这个被移除的元素
5. clear()，清空列表

---


```python
len(songs)
```




    14




```python
songs.index('亲爱的')
```




    2




```python
songs.reverse()
songs
```




    ['童年',
     '我真的受伤了',
     '脆弱的一分钟',
     '当冬夜渐凉',
     '残缺的彩虹',
     '100种生活',
     '红豆',
     '流年',
     '飞',
     '水星记',
     '艺术家',
     '亲爱的',
     '光',
     '像我这样的人']




```python
songs.pop()
```




    '像我这样的人'




```python
songs.clear() #清空之后只剩空列表
songs
```




    []




```python
del songs #直接删除songs列表
```


```python
songs
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-29-52246b9ab6d4> in <module>
    ----> 1 songs
    

    NameError: name 'songs' is not defined


---
# 元组 tuple

元组可以用tuple()函数创建，也可以直接用括号（单个元素时需要加逗号分割）形式创建。

列表是可变类型，允许我们随意改动，而元组是不可变类型，也就是说我们定义了这个元组，是固定的，不可以变的。


```python
songs = ('像我这样的人','光','孤独之书','艺术家','水星记','飞','流年','红豆','100种生活',
        '残缺的彩虹','毒苹果','当冬夜渐凉','脆弱的一分钟','我真的受伤了')
```

## 查


```python
songs[0]
```




    '像我这样的人'




```python
songs[3:6]
```




    ('艺术家', '水星记', '飞')




```python
songs[-2]
```




    '脆弱的一分钟'



---
## 改（报错）


```python
songs[0] = '北极星的眼泪'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-36-4b167b934d90> in <module>
    ----> 1 songs[0] = '北极星的眼泪'
    

    TypeError: 'tuple' object does not support item assignment


---
## 删
删除元组内元素同样会报错。但是，可以删除整个元组。


```python
del songs[1]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-37-e51ee88648ab> in <module>
    ----> 1 del songs[1]
    

    TypeError: 'tuple' object doesn't support item deletion



```python
del songs
```

---
## 增（报错）
增也是一个道理，元组是不可变类型，所以我们没办法对里面的元素进行操作的，如果硬要往里面添加内容，我们只能再搞一个元组，然后合并进去。


```python
('孤单',) + songs 
```




    ('孤单',
     '像我这样的人',
     '光',
     '孤独之书',
     '艺术家',
     '水星记',
     '飞',
     '流年',
     '红豆',
     '100种生活',
     '残缺的彩虹',
     '毒苹果',
     '当冬夜渐凉',
     '脆弱的一分钟',
     '我真的受伤了')



# 选择列表还是元组？

    我们知道list和tuple都是一个存放元素的有序列表，但列表和元组他们不一定存储相同数据类型的元素，也可同时存储int，float，string等类型。
    
    数据结构，说白了就是把数据安排好，安排的妥妥的。所以在不同的场景下我们需要不同的数据结构来“安排”好数据。
    
    而数据的存储就会涉及到内存。当我们定一个元组的时候，定义完之后，内存是固定不变的，而我们定义一个列表，内存是可以随着我们的操作而改变的。
    
    这个时候你就知道了，列表是用来存储那些比较“灵活”的元素的，而元组是用来存储那些比较“死板”的元素的。


```python
my_tuple = (1,2.0,'abc')
my_list = [1,2.0,'abc']
print('my_tuple size: ',my_tuple.__sizeof__())
print('my_list size: ',my_list.__sizeof__())

```

    my_tuple size:  48
    my_list size:  64
    


```python
my_list.insert(1,'[1,2,3]')
print('my_list size: ',my_list.__sizeof__())
```

    my_list size:  96
    

---
列表和元组的转换也非常便捷。


```python
my_list0 = [1,2,3,4]
my_tuple = tuple(my_list0)
my_tuple
```




    (1, 2, 3, 4)




```python
my_list = list(my_tuple)
my_list
```




    [1, 2, 3, 4]



---
# 字典 dict

字典由key：vaule组成，像这样：
    
    dict = {'name':'handsomeb','Age':18'}
    
可以看到，字典是由{}大括号来封装元素的。这里的name和Age叫做key，handsomeb和18就叫做vaule。

在这种数据结构中，key只能用不可变类型，而vaule可以使用可变类型。因为在字典中，我们的key是不能重复的，这样我们才能通过key来查找对应的唯一值。


```python
# 将列表作为key时，报错。
dict = {[1,2,3]:'abc'}
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-3-9f275626f892> in <module>
    ----> 1 dict = {[1,2,3]:'abc'}
    

    TypeError: unhashable type: 'list'



```python
# 而将元组作为key时，是可以的。
dict = {(1,2):'abc'}
```

---
## 查


```python
dict = {'name':'handsomeb','age':18,'len':8}
```


```python
dict['name'],dict['age']
```




    ('handsomeb', 18)



---
## 改


```python
dict['len'] = 11
dict
```




    {'name': 'handsomeb', 'age': 18, 'len': 11}



---
## 删
删除字典由几种操作。


```python
# 1.删掉字典中的其中一个元素
del dict['len']
dict
```




    {'name': 'handsomeb', 'age': 18}




```python
# 2. 清空字典中的元素
dict.clear()
dict
```




    {}




```python
# 3. 删除字典
my_dict = {'name':'mars','age':27}
del my_dict
my_dict
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-12-b1cc62b1f6f9> in <module>
          2 my_dict = {'name':'mars','age':27}
          3 del my_dict
    ----> 4 my_dict
    

    NameError: name 'my_dict' is not defined


---
## 增



```python
my_dict =  {'name':'mars','age':27}
my_dict
```




    {'name': 'mars', 'age': 27}




```python
my_dict['len'] = 18
my_dict
```




    {'name': 'mars', 'age': 27, 'len': 18}



---
## 字典和列表及元组之间的转换

dict.values(),将字典中的value转换成列表；

dict.keys(),将字典中的key转换成列表；

dict.items(),将字典中的元组转换成元组；


```python
my_dict = {'name': 'mars', 'age': 27, 'len': 18}
```


```python
my_dict.values()
```




    dict_values(['mars', 27, 18])




```python
my_dict.keys()
```




    dict_keys(['name', 'age', 'len'])




```python
my_dict.items()
```




    dict_items([('name', 'mars'), ('age', 27), ('len', 18)])



---
# 集合 set

集合和字典差不多，不过集合没有键对值，也是使用大括号{}。像这样：

    set = {1，2.0，'abc'}
    
set这种数据结构，里面的元素都是唯一的，无序的，不可以重复的，并且用的是不可变类型，比如number类型、tuple类型，以及string类型。

定义集合，有两种方式，一种是直接定义：

    my_set = {1,2,3}
 
另一种是使用set方法，也就是将其他类型转换成set：

    my_set = set((1,2,3))
    my_set = set([1,2,3])

---
## 查（出错）

原因是set集合不支持索引操作，因为他是无序的。

通常查询集合，更多是使用in和not in关键字查询。


```python
my_set = set([1,2,3,4,5,4,4,6])
my_set
```




    {1, 2, 3, 4, 5, 6}




```python
my_set[1]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-22-d447519d8314> in <module>
    ----> 1 my_set[1]
    

    TypeError: 'set' object is not subscriptable



```python
1 in my_set
```




    True




```python
7 not in my_set
```




    True



---
## 增

想要在集合里添加元素，可以调用set的add方法。


```python
a = {1,2,3,4}
a.add(5)
a
```




    {1, 2, 3, 4, 5}




```python
a.add('abc')
a
```




    {1, 2, 3, 4, 5, 'abc'}




```python
a.add((1,))
a
```




    {(1,), 1, 2, 3, 4, 5, 'abc'}



---
## 改

set不支持索引，所以没办法通过索引去修改其中的元素，set有一个update方法，我们可以使用他来追加元素到集合中。


```python
b = {1,2,3}
b.update('a')
b
```




    {1, 2, 3, 'a'}




```python
b.update(['a','b','c'])
b
```




    {1, 2, 3, 'a', 'b', 'c'}




```python
b.update((4,5,6))
b
```




    {1, 2, 3, 4, 5, 6, 'a', 'b', 'c'}



---
## 删

想要删除集合中的元素，可以使用remove方法，也可以使用discard方法。两者的区别是，discard指定的元素即使不存在也不会报错。

清空集合的元素，可以使用clear方法。删除集合，可以使用del函数。

以及，求两个集合的并集，可以使用union方法、交集使用intersection方法、子集使用issubset方法和父集使用issuperset方法。


```python
c = set((1,2,3,3,4,5,6))
c
```




    {1, 2, 3, 4, 5, 6}




```python
c.remove(1)
c

```




    {2, 3, 4, 5, 6}




```python
c.discard(2)
c
```




    {3, 4, 5, 6}




```python
c.discard(1)
```


```python
c.clear()
c
```




    set()




```python
del c
c
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-39-d5e7b9e5f2ed> in <module>
          1 del c
    ----> 2 c
    

    NameError: name 'c' is not defined



```python
set_0 = {1,2,3,4,5}
set_1 = {3,4,5,6,7}
```


```python
set_0.union(set_1)
```




    {1, 2, 3, 4, 5, 6, 7}




```python
set_0.intersection(set_1)
```




    {3, 4, 5}




```python
set_2 = {1,2,3}
set_3 = {1,2,3,4,5}
```


```python
set_2.issubset(set_3)
```




    True




```python
set_3.issuperset(set_2)
```




    True




