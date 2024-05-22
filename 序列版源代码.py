###视频音频合并功能依赖于FFmpeg开源工具，本程序仅充当“启动器”的角色，旨在帮助用户快捷使用FFmpeg的视频音频合并功能
import tkinter as tk
from tkinter import filedialog
import subprocess
from tkinter import messagebox

commands_list = []  # 初始化命令列表

def generate_command():  # 生成命令函数，获取用户输入的视频文件、音频文件和输出文件路径

    video_file = entry_video.get()  # 获取视频文件路径
    audio_file = entry_audio.get()  # 获取音频文件路径
    export_file = entry_export.get()  # 获取输出文件路径

    # 如果有任一字段为空，提示用户填写所有字段  
    if not (video_file and audio_file and export_file):
        messagebox.showerror("错误", "请填写所有文件的地址")
        return

    # 构建 FFmpeg 命令，将视频文件、音频文件和输出文件路径添加到命令中
    command = f"ffmpeg -i \"{video_file}\" -i \"{audio_file}\" -codec copy \"{export_file}\""
    commands_list.append(command)  # 将命令添加到命令列表中
    update_command_text()  # 更新命令显示文本框


def clear_commands():  # 清空命令列表函数
    
    commands_list.clear()  # 清空命令列表
    update_command_text()  # 更新命令显示文本框


def update_command_text():  # 更新命令显示文本框函数

    command_text.delete('1.0', tk.END)  # 清空文本框内容

    # 遍历命令列表，将每个命令添加到文本框中，并换行
    for command in commands_list:
        command_text.insert(tk.END, command + '\n')  # 向文本框中插入文本
    command_text.see(tk.END)  # 滚动到文本框底部


def run_commands():  # 运行命令函数

    # 打开一个名为 "commands.bat" 的文件，以写入模式打开，文件句柄为 f
    with open("commands.bat", "w") as f:
        
        # 使用 enumerate 函数遍历命令列表中的每个命令及其索引
        for i, command in enumerate(commands_list):
            f.write(command)  # 将当前命令写入文件中

            # 如果不是最后一个命令，则在其后添加 "&&" 运算符
            if i < len(commands_list) - 1:
                f.write(' && ')

    subprocess.run("commands.bat", shell=True)  # 执行批处理文件


def browse_file(entry):  # 浏览文件函数
    
    filename = filedialog.askopenfilename()  # 弹出文件选择对话框，获取文件路径并存储在filename中
    entry.delete(0, tk.END)  # 清空输入框中的所有文本内容
    entry.insert(0, filename)  # 将filename插入到文本输入框的开头位置，即在第一个字符处开始插入文件路径
    entry.xview_moveto(1.0)  # 横向滚动文本输入框，使其内容水平滚动到最右侧（这个倒霉函数以0.0为最左侧，1.0为最右侧）


def reset_entry(entry):  # 重置文本框函数
    
    entry.delete(0, tk.END)  # 删除输入框中的所有文本


root = tk.Tk()  # 创建根窗口对象
root.geometry("500x600")  # 设置根窗口的尺寸
root.title("【天津市第二原神学校】视频音频合并工具")  # 设置根窗口的标题

# 创建一个 Frame，用于放置界面上方的部件
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

# 创建标签，用于显示 "视频文件:"，并将其放置在 frame_top 中的第一行第一列
label_video = tk.Label(frame_top, text="视频文件:")
label_video.grid(row=0, column=0, padx=10)

# 创建一个文本输入框，用于用户输入视频文件路径，宽度为 30
entry_video = tk.Entry(frame_top, width=30)
entry_video.grid(row=0, column=1)  # 放置在 frame_top 中的第一行第二列

# 创建按钮，显示 "浏览"，点击后调用 browse_file 函数来选择视频文件
button_video = tk.Button(frame_top, text="浏览", command=lambda: browse_file(entry_video))
button_video.grid(row=0, column=2)  # 放置在 frame_top 中的第一行第三列

# 创建重置按钮，用于清空视频文件输入框
button_reset_video = tk.Button(frame_top, text="重置", command=lambda: reset_entry(entry_video))
button_reset_video.grid(row=0, column=3)  # 放置在 frame_top 中的第一行第四列

# 创建类似的标签、文本输入框和按钮，用于音频文件
label_audio = tk.Label(frame_top, text="音频文件:")
label_audio.grid(row=1, column=0, padx=10)
entry_audio = tk.Entry(frame_top, width=30)
entry_audio.grid(row=1, column=1)
button_audio = tk.Button(frame_top, text="浏览", command=lambda: browse_file(entry_audio))
button_audio.grid(row=1, column=2)

# 创建重置按钮，用于清空音频文件输入框
button_reset_audio = tk.Button(frame_top, text="重置", command=lambda: reset_entry(entry_audio))
button_reset_audio.grid(row=1, column=3)  # 放置在 frame_top 中的第二行第四列

# 创建类似的标签、文本输入框和按钮，用于输出文件
label_export = tk.Label(frame_top, text="输出文件:")
label_export.grid(row=2, column=0, padx=10)
entry_export = tk.Entry(frame_top, width=30)
entry_export.grid(row=2, column=1)
button_export = tk.Button(frame_top, text="浏览", command=lambda: browse_file(entry_export))
button_export.grid(row=2, column=2)

# 创建重置按钮，用于清空输出文件输入框
button_reset_export = tk.Button(frame_top, text="重置", command=lambda: reset_entry(entry_export))
button_reset_export.grid(row=2, column=3)  # 放置在 frame_top 中的第三行第四列

# 创建按钮，用于触发生成命令函数
button_generate = tk.Button(root, text="生成命令", command=generate_command)
button_generate.pack(pady=10)

# 创建一个 Frame，用于放置命令文本框和滚动条
command_text_frame = tk.Frame(root)
command_text_frame.pack(fill=tk.BOTH, expand=True)

# 创建垂直滚动条，并放置在命令文本框的右侧
scrollbar = tk.Scrollbar(command_text_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# 创建文本框，用于显示生成的命令，设置 wrap 为 NONE，防止自动换行
command_text = tk.Text(command_text_frame, wrap=tk.NONE, yscrollcommand=scrollbar.set)

# 将文本框填充满整个父容器，并可扩展
command_text.pack(fill=tk.BOTH, expand=True)

# 配置滚动条，使其与文本框的垂直滚动关联
scrollbar.config(command=command_text.yview)

# 创建按钮，用于触发运行命令函数
button_run = tk.Button(root, text="运行命令", command=run_commands)
button_run.pack(pady=10)

# 创建按钮，用于清空命令列表
button_clear = tk.Button(root, text="清空序列", command=clear_commands)
button_clear.pack(pady=10)

# 进入 Tkinter 主事件循环
root.mainloop()
