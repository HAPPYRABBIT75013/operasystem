#update log----------------0.0.0
#add basic codes,import os
import os
import pygame
import sys
print("welcome to the OS!Now ,you can use it!!!")
while True:
    input_code = input(">>>")
    if input_code == 'help':
        print("欢迎使用本窗口，没想到吧，此OS支持（仅支持)中文呦""但由于python的问题，所以暂且还是需要输入英文指令~~~")
        pygame.time.delay(100)
        print("about:关于此OS" "  ""help：显示此帮助" "  " "exit：退出此OS" "  " "open:打开文件" "math:打开计算器" "" "(\请用双斜杠代替)")
    elif input_code == "exit":
        print("再见")
        pygame.time.delay(100)
        exit()
    elif input_code == "about":
        print("版本号：0.0.0")
    #未知问题 unknown errorelif input_code == "open":
        #未知问题 unknown error  path = input("请输入文件路径及文件名")
    #未知问题 unknown error os.system(path)  # path为文件路径，本目录下可直接写文件名os 为本地模块不需再行安装
    elif input_code == "math":
        check_math = print(os.system('C:\\Windows\\System32\\calc.exe'))
        print("已打开")
    elif input_code == "command":
        command = input("请输入指令")
        os.system(command)
        print("已执行")
    elif input_code == "remove":
        remove = input("删除文件路径及名称")
        os.remove(remove)
        print("已执行")