def print_file_info(file_name):
    f = None
    try:
        f = open("file_name","r",encoding="UTF-8")
        content = f.read()
        print(f"文件的全部内容:{content}")
    except Exception as e:
        print(f"出现异常了，异常信息是{e}")
    else:
        print("很好，没有异常")
    finally:
        if f:           # 开头定义了f为None，如果该文件不存在，则f还是为None，if语句就不会触发；否则if会触发
            f.close()
def append_to_file(file_name,data):
        f = open("file_name","a",encoding="UTF-8")
        f.write(data)
        f.write("\n")
        f.close()