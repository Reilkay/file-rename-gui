<p align="center">
  <h1 align="center">file-rename-gui</h1>
  <p align="center">A simple gui program for rename files.<p>
  <p align="center">
    <a href="https://blog.reilkay.com/about/"><img src="https://img.shields.io/badge/MADE--BY-Ray-blue?style=flat-square" alt="Binray • 二进制蕾伊"></a>
    <img src="https://img.shields.io/badge/VRESION-Release_1.0-critical?style=flat-square" alt="version Release 1.0">
  </p>
</p>





## 介绍

该项目主要用于批量修改文件名称。

现使用`Python`进行开发，使用`PySide6`实现图形界面。

## 项目背景

最近天天从网上下电视剧看，系统自带的批量重命名实在不尽如人意，文件后的序号会自带括号，又去网上找了一下现成的，要么界面过于复杂，要么就是缺少所需的功能，于是自己用python整了一个。

## 功能

功能十分单一，现仅能用于批量重命名，可以实现：

+ 根据文件后缀名筛选文件
+ 迭代添加多级文件夹中的文件
+ 不修改文件名仅修改后缀
+ 自定义序号位数和起始值
+ 撤销上一步操作（可使用快捷键Ctrl+Z）

## 使用

1. 克隆仓库后使用`python`解释运行。

2. 在[`Release`](https://github.com/Reilkay/file-rename-gui/releases)页面下载对应的二进制包使用。

## 想增加的功能（咕咕咕）

- [ ] 自定义序号格式

- [ ] 正则匹配筛选文件

etc.

​	\*今天可以可以整点pr吗
