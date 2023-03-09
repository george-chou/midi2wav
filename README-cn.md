# midi2wav

[![license](https://img.shields.io/github/license/george-chou/midi2wav.svg)](https://www.gnu.org/licenses/lgpl-3.0.en.html)
[![Python application](https://github.com/george-chou/midi2wav/actions/workflows/python-app.yml/badge.svg)](https://github.com/george-chou/midi2wav/actions/workflows/python-app.yml)

64 位 Win10 下的一款基于 SF2 音源的将 MIDI 渲染成 WAV 的 Python 脚本

## 前置安装
```
pip install midi2audio
pip install xpinyin
```

## 使用方法

01. 安装 <a href="https://www.123pan.com/s/Hl2SVv-EbWRh.html" target="_blank">fluidsynth-2.2.4-win10-x64</a>;

1. 下载 <a href="https://www.123pan.com/s/Hl2SVv-kbWRh.html" target="_blank">soundfonts</a> 放入 `./sf` 文件夹;

2. 将要渲染的 MIDI 文件放入 `./input` 文件夹;(若 MIDI 文件名含有中文字符，请放入后运行一下 `rename.py`，重命名前的 MIDI 将备份到 `./backup` 路径)

3. 按此示例格式跑如下命令:
```
python render.py --sf "./sf/J800 Piano.sf2"
```
4. 将渲染出的 WAV 文件从 `./output` 文件夹中取出。