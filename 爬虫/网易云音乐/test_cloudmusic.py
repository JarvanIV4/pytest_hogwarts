# -*- coding: utf-8 -*-
# @Time : 2020/03/08
# @Author : Wind
# cloudmusic.PYPI网址：https://pypi.org/project/cloudmusic/
import cloudmusic


music = cloudmusic.getMusic(459115010)

# 通过歌曲id获取Music对象，并展示部分属性
print("歌名：{}".format(music.name))
print("歌手：{}".format(music.artist))
print("音频文件url：{}".format(music.url))

# 获取一首歌的热评并展示部分信息
coms = music.getHotComments()
for com in coms:
    print("发布者：{}".format(com['nickName']))
    print("内容：{}".format(com['content']))
    print("获赞数：{}".format(com['likeCount']))
    print("------------")



# 通过关键字搜索获取前10首歌曲的Music对象，并输出每首歌的评论数量
results = cloudmusic.search("白日", 10)

for music in results:
    print(music.getCommentsCount())

# 通过歌单id获取Music对象列表，并下载整个歌单的无损品质音频
path = 'D:\\网易云音乐-歌单\\'
playlist = cloudmusic.getPlaylist(3103264115)
for music in playlist:
    music.download(dirs=path, level="standard")  # standard：标准; lossless：无损