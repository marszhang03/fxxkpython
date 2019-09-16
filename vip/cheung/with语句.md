
# with语句

    在with调用后得到的对象里面需要用__enter__()和__exit__()这两个方法，也就是说，如果你想要让你创建的对象能被with使用，那么你这个对象必须要有__enter__()和__exit__()这两个方法。

## with...open()...as...
    在文件操作中，我们到最后都需要关闭这个文件流的，但是又with语句之后，Python直接在里面做了资源关闭操作，我们就不需要手动去关闭了。

### 例如：


```python

with open('test.txt','w') as f:
    f.write('abcdefg')
```

---
## 例子1

    可以看到，我们使用with调用get_Handsomeb,得到的这个对象先执行“进入enter方法”，再执行with里面的“Get...”，都执行完毕之后，再去执行“进入exit方法”。


```python
class Handsomeb:
    def __enter__(self):
        print("进入enter方法")
    
    def __exit__(self,type,value,trace):
        print('进入exit方法')
        
def get_Handsomeb():
    return Handsomeb()

with get_Handsomeb():
    print('Get...')
```

    进入enter方法
    Get...
    进入exit方法
    

---
## 例子2
    with...后面紧跟的as是干嘛的？
    在这里的as后面的变量名称，其实得到的就是enter方法返回的值。



```python
class Handsomeb:
    def __enter__(self):
        print("进入enter方法")
        return "Handsomeb"
    
    def __exit__(self,type,value,trace):
        print('进入exit方法')
        
def get_Handsomeb():
    return Handsomeb()

with get_Handsomeb() as h:
    print('h: ',h)
```

    进入enter方法
    h:  Handsomeb
    进入exit方法
    

---
也可以返回一个对象。


```python
class Handsomeb:
    def __enter__(self):
        print("进入enter方法")
        return self
    
    def __exit__(self,type,value,trace):
        print('进入exit方法')
        
def get_Handsomeb():
    return Handsomeb()

with get_Handsomeb() as h:
    print('h: ',h)
```

    进入enter方法
    h:  <__main__.Handsomeb object at 0x0000020107B1BD68>
    进入exit方法
    

---
## 例子3
    我们看看定义的这个__exit__方法，这里携带了几个参数：type，value，trace。他是干嘛的呢？我们在操作一些对象的时候，比如操作文件的时候，可能会发现这样那样未知的异常，比如文件的位置找不到了，文件打不开了等等问题，关于这些异常的信息，我们可以在__exit__方法中找到。


```python
class Handsomeb:
    def __enter__(self):
        print("进入enter方法")
        return self
    
    def __exit__(self,type,value,trace):
        print('进入exit方法')
        print('type: ',type)
        print('value: ',value)
        print('trace',trace)
        return True
    
    def cal(self):
        return 100/0
        
def get_Handsomeb():
    return Handsomeb()

with get_Handsomeb() as h:
    h.cal()
```

    进入enter方法
    进入exit方法
    type:  <class 'ZeroDivisionError'>
    value:  division by zero
    trace <traceback object at 0x0000020107B1E188>
    

---
# 总结
    
    以上就是with语句的工作方法，简单点说，enter方法做了一些初始化操作，exit做了一些擦屁股的操作。


```python

```
