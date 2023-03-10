# midi2wav

[![license](https://img.shields.io/github/license/george-chou/midi2wav.svg)](https://www.gnu.org/licenses/lgpl-3.0.en.html)
[![Python application](https://github.com/george-chou/midi2wav/actions/workflows/python-app.yml/badge.svg)](https://github.com/george-chou/midi2wav/actions/workflows/python-app.yml)

A Python script for rendering MIDI into WAV by SF2 on Windows 10 x64

## Requirements
```
pip install midi2audio
pip install xpinyin
```

## Usage

0. Install <a href="https://www.123pan.com/s/Hl2SVv-EbWRh.html" target="_blank">fluidsynth-2.2.4-win10-x64</a>;

1. Download <a href="https://www.123pan.com/s/Hl2SVv-kbWRh.html" target="_blank">soundfonts</a> into `./sf` directory;

2. Put your MIDI files into `./input` directory;(If not exist, create one)

3. Run the following command as an example:
```
python render.py --sf "./sf/J800 Piano.sf2"
```
1. Fetch WAV audios from `./output` path.

## Workflow
```
MIDI input -(add order)-> ordered -(to valid name)-> renamed -(render)-> output WAV
```