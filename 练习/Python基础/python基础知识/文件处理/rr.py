# -*- coding: utf-8 -*-
# @Time : 2020/8/15
# @Author : Wind
import os
import zipfile

def ZIPData(resources_dir, zip_name):
    dest = os.path.join(os.path.split(resources_dir)[0], '%s.zip' % (os.path.basename(resources_dir)))
    empty_dirs = []
    lenDirPath = len(os.path.split(resources_dir)[0])
    zipf = zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(resources_dir):
        empty_dirs.extend([dir for dir in dirs if os.listdir(os.path.join(root, dir)) == []])
        base = os.path.basename(root)
        for file in files:
            ph = os.path.join(root, file)
            zipf.write(ph, ph[lenDirPath:])

        for dir in empty_dirs:
            ph = os.path.join(root, dir)
            zif = zipfile.ZipInfo(ph[lenDirPath:] + "/")
            zipf.writestr(zif, "")
        empty_dirs = []
    zipf.close()


if __name__ == '__main__':
    resources_dir = r"/练习/Python基础/python基础知识/文件处理/resources"
    ZIPData(resources_dir)