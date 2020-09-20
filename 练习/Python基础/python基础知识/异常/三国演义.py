# 计算文件大致包含多少个单词

file_name = "三国演义.txt"
try:
    with open(file_name, encoding='utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file '" + file_name + "' does not exist."
    print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file '" + file_name + "' has about " + str(num_words) + " words.")
