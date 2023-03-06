from xpinyin import Pinyin
import os


def Q2B(uchar):
    """单个字符 全角转半角"""
    inside_code = ord(uchar)
    if inside_code == 0x3000:
        inside_code = 0x0020
    else:
        inside_code -= 0xfee0
    if inside_code < 0x0020 or inside_code > 0x7e:  # 转完之后不是半角字符返回原来的字符
        return uchar
    return chr(inside_code)


def stringQ2B(ustring):
    """把字符串全角转半角"""
    return "".join([Q2B(uchar) for uchar in ustring])


def tranSpecial(ustring):
    ustring = ustring.replace('【', '[')
    ustring = ustring.replace('】', ']')
    ustring = ustring.replace('·', '.')
    ustring = ustring.replace('「', '[')
    return ustring.replace('」', ']')


def rename(resume_rootdir='.'):
    print(u'重命名开始！')
    pin = Pinyin()
    llist = os.listdir(resume_rootdir)
    for i in range(0, len(llist)):
        print(u'现在进行第{}个'.format(i))
        resume = os.path.join(resume_rootdir, llist[i])
        if os.path.isfile(resume):
            obj = os.path.basename(resume)
            if obj[0] == '.':
                continue

            print(u'开始处理  {}'.format(obj))
            pinyin_name = pin.get_pinyin(
                obj.encode('utf-8').decode('utf-8'), "")
            pinyin_name = tranSpecial(stringQ2B(pinyin_name))
            print(u'{} 新名字是:{}'.format(obj, pinyin_name))
            Newdir = os.path.join(resume_rootdir, pinyin_name)  # 新的文件路径
            os.rename(resume, Newdir)  # 重命名
    print(u'重命名结束！')


if __name__ == "__main__":
    rename('./input')
