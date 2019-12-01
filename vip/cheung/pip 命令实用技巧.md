
# pip 命令实用技巧

1. pip install >模块名（例如requests）
2. pip --version >查看pip版本
3. pip install --upgrade pip >升级pip到最新版本
4. 在不同python版本中安装
   4.1 python2 -m pip install reqeusts
   4.2 python3 -m pip install reqeuets
5. pip install "requests==2.18.1" >安装指定版本的第三方模块
6. pip install --upgrade requests >升级模块到最新版本
7. pip show requests >查看第三方模块的具体信息
8. pip list >查看pip都安装了什么第三方模块
9. pip uninstall requests >卸载第三方模块
10. pip freeze>requirement.txt >生成项目的模块安装列表
11. pip install -r requirement.txt >一键安装文件中涉及到的所有模块
12. pip help >查看pip命令获取相关帮助
13. pip install -i 镜像地址 模块名 >改变pip下载源
