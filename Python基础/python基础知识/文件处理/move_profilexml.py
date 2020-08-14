# -*- coding: utf-8 -*-
# @Time : 2020/8/14
# @Author : Wind
import zipfile
import shutil
import os

username = "xjd_"
number = 1
num = str(number).zfill(3)


def create_hwics(profilexml_path, resources_dir):
    information_dir = resources_dir + "\\information"
    shutil.copy(profilexml_path, information_dir)
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
    filename = username + num + ".hwics"
    os.unlink(filename)
    os.rename(dest, filename)


if __name__ == '__main__':
    profilexml_path = "D:\Program Data\python_work\python_practice\Python基础\python基础知识\文件处理\profile.xml"
    resources_dir = r"D:\Program Data\python_work\python_practice\Python基础\python基础知识\文件处理\resources"
    create_hwics(profilexml_path, resources_dir)
