
# print函数

print函数在编程中经常使用，我们可以用它打印出信息。

1. print 使用 end参数，定义字符串结尾。默认是“\n”


```python
print('mars is coding',end='!')
```

    mars is coding!

---
2. print 使用 sep，定义字符串连接符号。默认是空格。




```python
print('mars','is','coding')
```

    mars is coding
    


```python
print('mars','is','coding.',sep = '_')
```

    mars_is_coding.
    


```python
print('C:','Windows','system32',sep = '\\')
```

    C:\Windows\system32
    

---
3. print 巧用format和f-string


```python
print('mars今年{}'.format(28))
```

    mars今年28
    


```python
age = 28
print(f'mars今年{age}')
```

    mars今年28
    

---
4. print的另一种格式化%



```python
print('%s今年%d岁.'%('mars',28))
```

    mars今年28岁.
    

---
5. print 可以打印各种类型信息


```python
list = [1,2,3,4]
tuple = (1,2)
num = 8
print(list)
print(tuple)
print(num)
```

    [1, 2, 3, 4]
    (1, 2)
    8
    


```python
class Person:
    def __init__(self,name,age):
        self.age = age
        self.name = name
```


```python
print(Person('mars','28')) # 打印出的是对象的地址值
```

    <__main__.Person object at 0x000001DE69F1D978>
    


```python
class Person:
    def __init__(self,name,age):
        self.age = age
        self.name = name
    
    # 定义__str__方法，这样在执行print的时候，他会先去执行str方法，从而打出出信息。
    def __str__(self):
        return f"Person 的信息是:\n name:{self.name}\n age:{self.age}"
```


```python
print(Person('mars','28'))
```

    Person 的信息是:
     name:mars
     age:28
    


```python

```


```python

```
