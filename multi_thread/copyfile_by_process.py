import os
from multiprocessing import Process


def copy_file(source_dir, dest_dir, file_name):
    src_path = source_dir + "\\" + file_name
    dest_path = dest_dir + "\\" + file_name

    with open(src_path, "rb") as source_file:
        with open(dest_path, "wb") as dest_file:
            # 循环读取源文件内容
            while True:
                data = source_file.read(1024)
                # 如果读到数据，就写入目标文件
                if data:
                    dest_file.write(data)
                else:
                    break


if __name__ == '__main__':

    source_dir = "../../../PythonCrawlerProject_ProxyPool/demo-thread/Python进阶 - 多线程编程入门"
    dest_dir = "D:\\__test_data_tmp\\tmp_test1"

    try:
        os.mkdir(dest_dir)
    except:
        print("目标目录已经存在")

    file_list = os.listdir(source_dir)
    for file_name in file_list:
        copy_process = Process(target=copy_file, args=(source_dir, dest_dir, file_name))
        copy_process.start()
