
# lambda 匿名函数

lambda 匿名函数格式：lambda 参数1、参数2、参数3...参数n : 表达式

lambda 匿名函数适用于即用即走的场景。

lambda 匿名函数传参：（lambda x,y:x+y)(1,2)


```python
# 例子1
(lambda x,y:x+y)(1,3)
```




    4




```python
# 例子2
(lambda *args:print(args))(1,2,3,4)
```

    (1, 2, 3, 4)
    


```python
# 例子3(遍历0-9这10个数字，然后依次交给匿名函数处理，处理的方式是x%2)
my_list = [(lambda x:x%2)(x) for x in range(10)]
print(my_list)
```

    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    


```python
dit = {'a':1,'b':2}
dit.items()
```




    dict_items([('a', 1), ('b', 2)])




```python
# 例子4（匿名函数赋值）
add = (lambda x,y:x+y)
print(add(1,2))
```

    3
    

## 匿名函数在啥时候用？

匿名函数在那些只需要执行一次就不要了的函数身上可以使用。在函数式编程中经常使用到。也就是说，我们可以通过匿名函数，结合python提供的map(),filter()函数进行高效使用。

    map函数：map(函数对象,序列)，也就是说，它可以传入两个参数，第一个可以传入函数，第二个传入序列。当执行这个函数的时候，序列里面的每个值都会被取出来，然后拿去执行传入的函数。
    
    filter函数：filter(函数对象,序列），同理，只不过filter中传入的函数对象一般用来作判断。


```python
# 例子1 (一般方式写法)
my_list = [1,2,3,4,5,6,7,8,9,10]

def add(x):
    return x+5

print(list(map(add,my_list)))
```

    [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    


```python
# 例子2 （配合lambda函数写法）
my_list = [1,2,3,4,5,6,7,8,9,10]
print(list(map((lambda x:x+5),my_list)))
```

    [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    


```python
# 例子3
my_list = [1,2,3,4,5,6,7,8,9,10]
print(list(filter((lambda x:x%2==0),my_list)))
```

    [2, 4, 6, 8, 10]
    


```python

```


```python

```
