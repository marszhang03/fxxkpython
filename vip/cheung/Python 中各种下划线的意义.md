
# Python 中各种下划线的操作

    例如 _、_xx、xx_、__xx、__xx__、_classname__xx

1. 只有一个下划线（_）


```python
# 例子1，_是有值的，_会指向最后一次执行的表达式

5+8
```




    13




```python
_+2
```




    15




```python
_
```




    15




```python
# 例子2，使用_来格式化变量的值，比如金额
a = 9_000_000_000
a
```




    9000000000




```python
# 例子3，在range函数中使用_

for _ in range(10):
    print(_,end='')
```

    0123456789

---
    2. 常见的__xx__ ,统称为“魔法函数”，这些函数是python内置的，可以直接拿来使用。不建议使用前后双下划线命名函数。
    
    例如：
    __init__ ,初始化函数
    __str__

---
    3. 单个下划线开头的_xx
    以单个下划线开头命名的方法或者变量，就是说明他是仅提供内部使用的。


```python
# 例子1,(将以下函数保存为my_func.py在当前路径下)

def my_func():
    print('test')
    
def _my_func():
    print('test')
```


```python
from my_func import *
```


```python
my_func()
```

    test
    


```python
_my_func() #弹出错误，没有定义，只能被模块内部使用。
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-11-1e78710e873b> in <module>
    ----> 1 _my_func()
    

    NameError: name '_my_func' is not defined


---
    4. 单个下划线结尾的 xx_
    python有许多关键词，比如def、return、class、pass这些，他们都是有特殊意义的，所以我们在定义变量或者方法的时候，不可以用他们来命名，如果一定要这么“作”，可以在后面加_。此方法强烈不建议。


```python
def = 1
```


      File "<ipython-input-12-09f57f03a914>", line 1
        def = 1
            ^
    SyntaxError: invalid syntax
    



```python
def_ = 1
```

---
    5. 连个下划线开头的命名：__xx
    这种命名方法更多是用在类的继承，通过两个下划线开头命名的成员，可以防止被子类重写。


```python
# 例子1

class Person():
    def __init__(self):
        self.name = 'mars'
        self.__age = 18

mars = Person()
print(mars.name)
# 实例化的时候，调用__age将报错，提示没有该属性。
print(mars.__age) 
```

    mars
    


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-14-5c594a111865> in <module>
          8 mars = Person()
          9 print(mars.name)
    ---> 10 print(mars.__age)
    

    AttributeError: 'Person' object has no attribute '__age'



```python
# 使用__dir__()函数打印出对象的属性，发现__age变成了_Person__age,故无法读取。
print(mars.__dir__()) 
```

    ['name', '_Person__age', '__module__', '__init__', '__dict__', '__weakref__', '__doc__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
    


```python
# 但可以使用_Person__age读取。
print(mars._Person__age)
```

    18
    


```python
# 所以子类继承也一样

class Person():
    def __init__(self):
        self.name = 'mars'
        self.__age = 28
        
class Son(Person):
    def __init__(self):
        super().__init__()
        self.name = 'xxxxx'
        self.__age = 29

s = Son()
print(s.name)
print(s.__age)
```

    xxxxx
    


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-18-432fcd4edd80> in <module>
         14 s = Son()
         15 print(s.name)
    ---> 16 print(s.__age)
    

    AttributeError: 'Son' object has no attribute '__age'



```python
print(s.__dir__())
```

    ['name', '_Person__age', '_Son__age', '__module__', '__init__', '__doc__', '__dict__', '__weakref__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
    


```python
print(s._Son__age)
```

    29
    

---
    6. 一个下划线+类名+两个下划线开头的命名：__classname__xx


```python
# 可以这样变相使用

_Person__name = 'mars'

class Person():
    def print_name(self):
        return __name

mars = Person()
print(mars.print_name())
```

    mars
    
