def check_fileExt(func):
    def wrapper(filename):
        # 获取小数点的下标
        dot = filename.index('.')
        # 一般小数点下标往后就是文件后缀名
        ext = filename[dot+1:]
        print('The file extension is {}.'.format(ext))
        func(filename)
    return wrapper
        
@check_fileExt
def create_file(filename):
    with open(filename,'w') as f:
        f.write('hahahha')

create_fileExt('test.txt')
