import tkinter as tk
from tkinter import filedialog
import os
"""
import os
def vplusa():
    v=input('vedio file:')
    a=input('audio file:')
    export=input('export file:')
    com=f"ffmpeg -i {v} -i {a} -codec copy {export}"
    print(com)

    with open("run.bat","w") as f:
        f.truncate(0)
        f.writelines(com)
    os.system("run.bat")

vplusa()

"""
# 主函数
def generate_command():
    video_file = entry_video.get()
    audio_file = entry_audio.get()
    export_file = entry_export.get()
    # 从输入框获取变量
    command = f"ffmpeg -i {video_file} -i {audio_file} -codec copy {export_file}"
    # 按命令格式合并变量
    with open("command.bat", "w") as f:
    # 打开批处理文件
        f.truncate(0)
        # 清空
        f.write(command)
        # 写入命令
    print('[log]generate:')
    print(command)
    # 输出日志
    os.system("command.bat")
    # 运行批处理文件
# 创建主窗口
root = tk.Tk()
root.geometry("400x150")
root.title("视频音频合并工具")

# 创建顶部 Frame 用于将UI组件顶部居中
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

# 创建视频文件输入框
label_video = tk.Label(frame_top, text="视频文件:")
label_video.grid(row=0, column=0, padx=10)
entry_video = tk.Entry(frame_top, width=30)
entry_video.grid(row=0, column=1)

# 创建音频文件输入框
label_audio = tk.Label(frame_top, text="音频文件:")
label_audio.grid(row=1, column=0, padx=10)
entry_audio = tk.Entry(frame_top, width=30)
entry_audio.grid(row=1, column=1)

# 创建输出文件输入框
label_export = tk.Label(frame_top, text="输出文件:")
label_export.grid(row=2, column=0, padx=10)
entry_export = tk.Entry(frame_top, width=30)
entry_export.grid(row=2, column=1)

# 创建按钮
button_generate = tk.Button(root, text="生成命令并运行", command=generate_command)
button_generate.pack(pady=10)

# 运行主循环
root.mainloop()
