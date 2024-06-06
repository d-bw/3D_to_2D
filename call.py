import subprocess
import os
import time
import uuid

def call_sikuli_script(path,filename):
    # 设置环境变量
    os.environ['FILE_NAME'] = str(filename)
    os.environ['PATH_TO_FOLDER'] = str(path)
    # 调用SikuliX脚本
    sikuli_script_path = 'test.sikuli'  # SikuliX脚本路径
    sikuli_jar_path = 'sikulix.jar'  # SikuliX可执行文件路径
    subprocess.run(['java', '-jar', sikuli_jar_path, '-r', sikuli_script_path])




if __name__ == "__main__":
    time.sleep(5)
    # 传递参数（stp文件路径与文件名）
    call_sikuli_script("C:\\auto_proj\\test","test04")
    