import time
import os
# 闪烁
def blink(marker, duration=1, pause=0.5):
    for i in range(5):
        marker.highlight(duration)
        time.sleep(pause)


#参数设置
PATH_TO_FOLDER = str(os.environ['PATH_TO_FOLDER'])
FILE_NAME = str(os.environ['FILE_NAME'])


# 1. TODO: 在电脑上找到对应的文件夹，路径为：`D:\PTC\START`。保留文件夹`export`，保留文件`config.pro`，`Exlog.txt`, `std.out`，其余文件全部删除。

# 2.打开Creo Parametric 4.0软件，软件地址为 `C:\Program Files\PTC\Creo 4.0\M090\Parametric\bin\parametric.exe`
doubleClick("creo_icon.png")
time.sleep(35)


# 3. TODO:  如果提示当前页面脚本发生错误 是否继续在本页面运行脚本 选择 是  并持续点击 是  共3次
wait(Pattern("confirm_yes.png").similar(.67))
click(Pattern("confirm_yes.png").similar(.59))
#关闭提示框与弹窗
time.sleep(1)
click()
time.sleep(1)
click()
time.sleep(1)
click()
time.sleep(2)
click()
#关闭弹窗
click(Pattern("close_icon.png").exact())
# 4. TODO: 如果弹出页面 Upgrade to the latest version of Creo 直接关闭页面 


# 等待10秒
#time.sleep(10)



# 5. 在功能栏中找到“冰盒子工具箱”，选择此功能。
ice_box = wait("ice_box.png")
#blink(ice_box, 0.5)
click("ice_box.png")

# 6. 在“冰盒子工具箱”中，找到文件转换器，选择“批量转换”。
data_exchanger = wait(Pattern("data_exchanger.png").similar(.64))
#blink(data_exchanger, 0.5)
click(Pattern("data_exchanger.png").similar(.67))

# 7. 将“输入，输出”按钮切换明确，选择“输入”。
file_exchanger = wait("file_exchanger.png")
#blink(file_exchanger, 0.5)
click("file_exchanger.png")
input_output = wait("output.png")
#blink(input_output, 0.5)
click("output.png")
# 8. TODO: 提前将文件夹中对应的step文件改名为stp文件。

# 9. TODO: 在工具栏中选择“主页”，点击“选择工作目录”，找到对应的文件夹，设置为“工作目录”（确保转换完成的文件可以自动保存到此文件夹）。

# 10. 点击“浏览”按钮，找到存有stp文件的文件夹，选中文件夹，点击“打开”。点击右边的“对勾✅”按钮，等待进度条完成。
click("file_exchanger.png")
browse = wait("watch.png")
#blink(browse, 0.5)
click("watch.png")

select_directory = wait(Pattern("select_dir.png").similar(.65))
#blink(select_directory, 0.5)



paste(PATH_TO_FOLDER)
type(Key.ENTER)
click("open_stp.png")

click("file_exchanger.png")


check_mark = wait("check.png")
#blink(check_mark, 0.5)
click("check.png")
time.sleep(5)


# 11.  转换完成后，页面会提示“共转换几个文件，成功几个，失败几个”，点击确定。
click("confirm.png")

# 12.  选择左上角的“主页”，点击新建。
click(Pattern("file.png").similar(.82))

click("new.png")
# 13.  在左边类型选择“装配”，右边子类型选择“设计”。
click("install.png")
click("design.png")

click("new_name.png")

# 获取当前鼠标位置
current_location = Env.getMouseLocation()

# 计算新的鼠标位置 (向左移动100个单位)
new_location = Location(current_location.x - 100, current_location.y)

# 按下鼠标左键
mouseDown(Button.LEFT)



paste(FILE_NAME)

# 14. 使用默认模板，点击确定。

doubleClick("confirm.png")

# 15.  进入工具栏，点击“冰盒子建模”，找到下面的“建模”，选择“一夜暴富”。

click("ice_box_modeling.png")



click("modeling.png")
click("rich.png")
# 16. 点击确定，页面会提示“一键组装功能将会自动把工作目录下所有零件都装配到组件中，你是否确定进行”。选择确定。
click("rich_confirm.png")

# 17.  回到工具栏，点击“同名绘图”。
click("ice_box_modeling.png")
click("draw.png")


# 18. 将页面上出现的图形全部选中（用鼠标选中），点击键盘删除键。
time.sleep(5)
# 定义框选区域的起始和结束位置
start_x, start_y = 500, 200  # 框选起点坐标
end_x, end_y = 1300, 700  # 框选终点坐标

# 将鼠标移动到起始位置并按下左键
mouseMove(Location(start_x, start_y))
mouseDown(Button.LEFT)

# 将鼠标移动到终点位置
mouseMove(Location(end_x, end_y))

# 释放左键
mouseUp(Button.LEFT)

type(Key.DELETE)


# 19. 再次回到功能栏，找到“冰盒子绘图”，点击“零件卡片”。
click("ice_box_draw.png")
click("puzzle_card.png")
# 20.  操作步骤：
#     - 第一步，找到“模型选择”点击。
#     - 第二步，刷新模型列表。
#     - 第三步，不选择第一个文件（ASM0001），其余都全选。
#     - 第四步，右边的批量出图，选择✅，确定。
click("bulk_output.png")
click("model_choose.png")
click("refresh_model_list.png")
click("remove_first_model.png")


click("bulk_output.png")

click("check.png")
# 21. 最后另存为dxf文件。
time.sleep(15)
click(Pattern("click_file.png").similar(.68))
click("save.png")


click("select.png")
wait("to_dxf.png")
click("to_dxf.png")
click("change_file_name.png")
# 获取当前鼠标位置
current_location = Env.getMouseLocation()

# 计算新的鼠标位置 (向左移动100个单位)
new_location = Location(current_location.x - 100, current_location.y)
# 按下鼠标左键
mouseDown(Button.LEFT)

paste("fin_"+FILE_NAME)
type(Key.ENTER)

wait("confirm.png")
click("confirm.png")

# 22. TODO: 关闭Creo Parametric 4.0软件
time.sleep(3)
click(Pattern("close_icon_2.png").exact())

time.sleep(1)
click()

time.sleep(2)

click("exit_confirm.png")

# 等待5秒
time.sleep(5)
