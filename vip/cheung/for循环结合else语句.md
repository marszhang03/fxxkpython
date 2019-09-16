
# for循环语句结合else

    for循环中的else语句，在for循环中结束后会被运行，但是如果for循环中有break语句的话，就会直接结束循环，不会执行else。那么，else的起的作用就是过滤。

---
以下是代码演示：


```python
for i in [0,1,2,3,4,5,6]:
    print(i)
else:
    print('这里是for循环中的else语句。')
```

    0
    1
    2
    3
    4
    5
    6
    这里是for循环中的else语句。
    

可以看到，他是执行完for循环语句之后，再运行else语句的。

---


```python
for i in [0,1,2,3,4,5]:
    print(i)
    if i > 3:
        break

else:
    print('这里是for循环中的else语句。')
```

    0
    1
    2
    3
    4
    

可以看到，运行到4之后跳出循环，而且，else语句没有执行。

---


```python
for i in [0,1,2,3,4,5]:
    if i == 3:
        continue
    print(i)

else:
    print('这里是for循环中的else语句。')
```

    0
    1
    2
    4
    5
    这里是for循环中的else语句。
    

可以看到，i等于3的时候，就跳出循环。不过，else语句被执行了。

---
## 例子1
在2-9的列表中获取到里面的质数，可以这样写。


```python
for i in range(2,10):
    for x in range(2,i):
        if i % x == 0:
            print(i,'不是质数，因为它除了被自身整除外，还能被这样：',x,' * ',int(i/x))
            break
    else:
        print(i,'就是质数！')
```

    2 就是质数！
    3 就是质数！
    4 不是质数，因为它除了被自身整除外，还能被这样： 2  *  2
    5 就是质数！
    6 不是质数，因为它除了被自身整除外，还能被这样： 2  *  3
    7 就是质数！
    8 不是质数，因为它除了被自身整除外，还能被这样： 2  *  4
    9 不是质数，因为它除了被自身整除外，还能被这样： 3  *  3
    

---
## 例子2
在2-9列表中获取到里面的奇数，可以这样写。


```python
for i in range(2,10):
    if i % 2 == 0:
        continue
    else:
        print("奇数是：",i)
```

    奇数是： 3
    奇数是： 5
    奇数是： 7
    奇数是： 9
    


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
