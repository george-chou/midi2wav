from xpinyin import Pinyin
import os
import re
import shutil


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


def filename_filter(ustring):
    dirty_stuff = ["\"", "\\", "/", "|", ":", "*", "<", ">", "?", "·"]
    for stuff in dirty_stuff:
        ustring = ustring.replace(stuff, "#")

    return ustring


def tranSpecial(ustring):
    return re.sub("[^\x00-\xff]", "#", ustring)


def rename(resume_rootdir='./ordered'):
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
            pinyin_name = stringQ2B(pinyin_name)
            pinyin_name = tranSpecial(pinyin_name)
            pinyin_name = filename_filter(pinyin_name)
            print(u'{} 新名字是:{}'.format(obj, pinyin_name))
            Newdir = os.path.join(resume_rootdir, pinyin_name)  # 新的文件路径
            os.rename(resume, Newdir)  # 重命名

    print(u'重命名结束！')


def copy_dir(src_path, target_path):

    if os.path.isdir(src_path):
        filelist_src = os.listdir(src_path)

        if len(filelist_src) == 0:
            print('No input file')
            return False

        if not os.path.exists(target_path):
            print('Target dir not exist, create one...')
            os.makedirs(target_path)

        if not os.path.isdir(target_path):
            print('Target path is not a dir')
            return False

        for file in filelist_src:
            path = os.path.join(os.path.abspath(src_path), file)
            if os.path.isdir(path):
                path1 = os.path.join(os.path.abspath(target_path), file)
                if not os.path.exists(path1):
                    os.mkdir(path1)
                copy_dir(path, path1)
            else:
                with open(path, 'rb') as read_stream:
                    contents = read_stream.read()
                    path1 = os.path.join(target_path, file)
                    with open(path1, 'wb') as write_stream:
                        write_stream.write(contents)

        return True

    else:
        return False


def add_order(wkspace='./ordered'):
    filelist_src = os.listdir(wkspace)
    count = 0
    for file in filelist_src:
        count += 1
        current_path = os.path.join(wkspace, file)
        ordered_path = os.path.join(wkspace, str(count) + '_' + file)
        os.rename(current_path, ordered_path)


def rm_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)


def rename_invalid_filename():
    rm_dir('./ordered')
    rm_dir('./renamed')
    rm_dir('./output')
    copy_dir(src_path='./input', target_path='./ordered')
    add_order(wkspace='./ordered')
    copy_dir(src_path='./ordered', target_path='./renamed')
    rename(resume_rootdir='./renamed')


if __name__ == "__main__":
    rename_invalid_filename()
