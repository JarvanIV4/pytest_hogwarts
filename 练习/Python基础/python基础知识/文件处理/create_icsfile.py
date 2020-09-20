# -*- coding: utf-8 -*-
# @Time : 2020/8/14
# @Author : Wind
import zipfile
import shutil
import os


class CreateICSFile:

    def __init__(self):
        self.username = "xjd_"
        self.number = 1
        self.num = str(self.number).zfill(3)
        self.filename = self.username + self.num
        self.filename_hwics = self.filename + ".hwics"
        self.hwics_path = "./hwics资料包" + self.filename_hwics
        self.resources_dir = r"resources资料包"
        self.zip_path = r".\zip资料包\\" + self.filename + ".zip"
        self.profilexml_path = "profile.xml"
        self.information_path = "resources资料包/resources/information"

    def create_file_main(self, file_format=None, times=1):
        """
        生成多个资料包
        :param times: 生成资料包的个数
        """
        for i in range(times):
            self.create_file(file_format)

    def create_file(self, file_format=None):
        """
        生成hwics或zip格式的资料包
        :param resources_dir:
        :param file_format: 生成资料包的文件格式，为zip则生成hwics和zip文件
        """
        self.move_profile()  # 替换资料包中的profile文件
        self.create_hwics()  # 生成hwics格式资料包
        if file_format == 'zip':  # 生成zip格式资料包
            self.hwics_to_zip()

    def move_profile(self):
        shutil.copy(self.profilexml_path, self.information_path)

    def compress_folder(self, folder_path, compress_path):
        '''
        :param folder_path: 文件夹路径
        :param compress_path: 压缩包路径
        '''
        zip = zipfile.ZipFile(compress_path, 'w', zipfile.ZIP_DEFLATED)
        dict = {}
        for path, dirNames, fileNames in os.walk(folder_path):
            fpath = path.replace(folder_path, '')
            for name in fileNames:
                fullName = os.path.join(path, name).encode(encoding='utf-8')
                name = fpath + '\\' + name
                zip.write(fullName, name)
        zip.close()

    def create_zip3(self, dir_path="./resources资料包/resources"):
        """

        :param dir_path:
        """
        dest = os.path.join(os.path.split(dir_path)[0], '%s.zip' % (os.path.basename(dir_path)))
        empty_dirs = []
        lenDirPath = len(os.path.split(dir_path)[0])
        zipf = zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(dir_path):
            # files = root.replace(dir_path, '')
            empty_dirs.extend([dir for dir in dirs if os.listdir(os.path.join(root, dir)) == []])
            # base = os.path.basename(root)
            for file in files:
                ph = os.path.join(root, file)
                zipf.write(ph, ph[lenDirPath:])
            for dir in empty_dirs:
                ph = os.path.join(root, dir)
                zif = zipfile.ZipInfo(ph[lenDirPath:] + "/")
                zipf.writestr(zif, "")
            empty_dirs = []
        zipf.close()

    def create_hwics(self):
        """
        将资料包的后缀名.zip重命名为.hwics，并移动到“hwics资料包”目录下
        :param resources_dir: 资料包解压后的resources文件夹路径
        """
        self.compress_folder(self.resources_dir, self.hwics_path)  # 生成zip格式资料包
        os.rename(self.hwics_path, self.filename_hwics)   # 将.zip格式的资料包改为.hwics格式资料包
        dest_hwics = r".\hwics资料包\\" + self.filename_hwics
        if os.path.exists(dest_hwics):
            os.unlink(dest_hwics)
        shutil.move("./" + self.filename_hwics, "hwics资料包")    # 移动资料包到“hwics资料包”这个目录下

    def hwics_to_zip(self):
        path = "zip资料包临时文件夹"
        dir_name = path + "/" + self.filename
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
        os.mkdir(dir_name)  # 创建空文件夹
        dest_hwics_path = path + "/" + self.filename + "/" + self.filename_hwics
        shutil.copyfile(r"./hwics资料包/"+self.filename_hwics, dest_hwics_path)    # 复制资料包到“zip资料包临时文件夹”这个目录下
        zip_dir = r"./zip资料包临时文件夹/" + self.filename
        self.compress_folder(zip_dir, self.zip_path)    #
        print("资料包创建成功:" + self.filename + ".zip")


if __name__ == '__main__':
    z = CreateICSFile()
    z.create_file('zip')
