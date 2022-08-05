from os import system

system("adb start-server") # 启动adb
system("cls")

a = 1
while a <= 1:
    print("测试版可能有bug，请在support.qq.com/products/410627中反馈\n")
    print("""【0】清理进程并退出【1】查看设备连接情况【2】重启至rec
【3】重启至fastboot【4】查看fastboot连接情况【5】刷入rec分区【6】刷入boot分区
【7】安装应用【8】临时启动(A/B分区设备)【9】停用应用(免root)【10】启用被停用的应用\n""")
    skna = int(input("请输入数字："))
    if(skna == 0): # 输入0则退出
        system("adb kill-server") #清除进程
        exit() 
    if(skna == 1):# 查看设备连接情况
        system("cls")
        system("adb devices")
        system("pause")
    if(skna == 2):# 重启至rec
        system("cls")
        print("重启中...")
        system("adb reboot recovery")
        print("已重启，请确认")
        system("pause")
    if(skna == 3):# 重启至fastboot
        system("cls")
        print("重启中...")
        system("adb reboot fastboot")
        print("已重启，请确认")
        system("pause")
    if(skna == 4):# 查看fastboot连接情况
        system("cls")
        system("fastboot devices")
        system("pause")
    if(skna == 5):# 刷入rec分区
        system("cls")
        print("刷入rec分区有风险，请三思而后行\n")
        system("pause")
        system("cls")
        print("请进入fastboot模式后继续\n")
        system("pause")
        reciN = input("请将rec镜像放置于主目录，并输入文件名：")
        astadb = f"fastboot flash recovery {reciN}"
        system(astadb)
        system("pause")
    if(skna == 6):# 刷入boot分区
        system("cls")
        print("刷入boot分区有风险，请确认")
        system("pause")
        system("cls")
        print("请进入fastboot模式后继续\n")
        system("pause")
        bootN = input("请将boot镜像放置于主目录，并输入文件名: ")
        booadb = f"fastboot flash boot {bootN}"
        system(booadb)
        print("已刷入，请确认")
        system("pause")
    if(skna == 7):# 安装应用
        system("cls")
        print("请在开发者选项中打开“USB安装应用”再继续！\n")
        system("pause")
        print()
        apkN = input("请把apk放置于程序主目录，并输入apk文件名: ")
        apkS = f"adb install {apkN}"
        print("如果手机提示是否安装，请确认")
        system(apkS)
        print("已安装，请确认")
        system("pause")
    if(skna == 8):# 临时启动(A/B分区设备)  （未经测试）
        system("cls")
        print("请在fastboot模式下继续")
        print()
        system("pause")
        system("cls")
        imgN = input("请将镜像放置于主目录，再输入文件名")
        fullimg = f"fastboot boot {imgN}"
        system(fullimg)
        system("pause")
    if(skna == 9):# 停用应用（免root）
        system("cls")
        appPack = input("请输入应用的包名: ")
        fullPack = f"adb shell pm disable-user {appPack}"
        print("停用中......")
        system(fullPack)
        print("停用完成，请确认是否已停用")
        system("pause")
    if(skna == 10): #启用被停用的应用
        system("cls")
        appPack = input("请输入应用的包名: ")
        fullPack = f"adb shell pm enable {appPack}"
        print("启用中......")
        system(fullPack)
        print("启用完成，请确认")
        system("pause")
    system("cls")