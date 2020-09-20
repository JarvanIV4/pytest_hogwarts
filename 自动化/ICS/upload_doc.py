# -*- coding: utf-8 -*-
# __author__: Wind
# 2020/9/20 22:21
import re
import time
import zipfile
import os
import shutil
import xml.etree.ElementTree as ET
class Upload:
    def get_csrf_token(self):
        csrf_token = re.findall('<meta name="_csrf" content="(.*)"/>', r.content.decode('utf8'))
        session.headers['X-CSRF-TOKEN'] = csrf_token

    def upload(self):
        url = ""
        headers = {}
        data = {"file_id": "0", "lang": "en"}
        files = {'file': open(hwics_file_path, 'rb')}
        self.get_csrf_token()
        self.send_post(url, data=data, headers, files=files)

    def run_main(self):
        time_start = time.time()
        for i in range(times):
            filename = CreateICSFile().create_icsfile_main()
            SupportTrial().upload(filename)
        time_end = time.time()
        m, s = divmod(round(time_end-time_start), 60)
        h, m = divmod(m, 60)
        print("共用时： %02d:%02d:%02d" % (h, m, s))

    def compress_folder(self, folder_path, compress_path, file_name):
        compress_folder_path = compress_path + file_name + ".zip"
        zip = zipfile.ZipFile(compress_folder_path, "w", zipfile)
        for path, dirname, filenames in os.walk(folder_path):
            fpath = path.replace(folder_path, '')
            for name in filenames:
                full_name = os.path.join(path, name).encode(edcoding='utf-8')
                name = fpath + '\\' +name
                zip.write(full_name, name)
        zip.close()



