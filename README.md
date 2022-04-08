# kakashi - File Doppelganger

`kakashi`，《火影忍者》中的天才忍者，因使用写轮眼复制了上千种忍术而被称为“拷贝忍者”，

该工具借用其名，以体现「快速创建文件分身」的功能，即：

**在保留原文件/目录结构的同时，批量替换指定文本，以生成另一份**



## 安装

```bash
pip install amk_kakashi
```



## 使用

* 显示帮助

```shell
$ kks
usage: kakashi [-h] [-d] [-v] [-V] [-f FROM_PATH] [-t TO_PATH] [-m MAP_PATH] [-r]

在保留原文件/目录结构的同时，批量替换指定文本，以快速创建文件分身

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           启用调试模式
  -v, --verbose         显示详细日志
  -V, --version         查看当前版本号
  -f FROM_PATH, --from_path FROM_PATH
                        准备分身的文件或目录的路径
  -t TO_PATH, --to_path TO_PATH
                        文件或目录分身后保存的路径
  -m MAP_PATH, --map_path MAP_PATH
                        分身时需要替换的内容映射文件路径，每一行为一条映射，每条映射的格式须为"旧文本 => 新文本"
  -r, --remove_if_exist
                        若保存的路径已存在文件，则直接将其删除
```



* 使用方法

```shell
$ kks -f <from_path> -t <to_path> -m <map_path> [-[d|v]]

# 示例（效果如图所示）
$ kks -f test_proj -t test_proj_2 -m test_proj_map.txt -dv
```

![](https://gitee.com/AndyM129/ImageHosting/raw/master/images/202204082245942.png)



## 更新记录

