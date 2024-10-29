def mode():
    '''main def only select '''
    if select == 1:
        add()
    elif select == 2:
        find()
    elif select == 3:
        revise()
    elif select == 4:
        delete()
    elif select == 5:
        display()
    elif select == 6:
        print("系統已退出。")
    else:
        print("錯誤，請重新輸入\n")


def add():
    '''add new employee'''
    data = {'department': None, 'name': None, 'age': None, 'phone': None}
    data["department"] = input("請輸入部門: ")
    data["name"] = input("請輸入姓名: ")
    data["age"] = input("請輸入年齡: ")
    data["phone"] = input("請輸入手機號碼: ")
    total.append(data)
    if input("是否繼續新增資料? (y/n): ") == "y":
        add()


def find():
    '''search someone info'''
    aim = input("請輸入要查詢的姓名:")
    data_switch = {}
    for t in total:
        if aim in t.values():
            for key, value in t.items():
                data_switch[value] = key
            print("\n--- 查詢結果 ---\n部門\t姓名\t年齡\t手機\n----------------------\
------------------")
            for value in t.values():
                print(value, end="\t")
            print()
            break
    if len(data_switch) == 0:
        print("查無此人")


def revise():
    '''change new info'''
    index = -1
    aim = input("請輸入要修改的姓名: ")
    data_switch = {}
    for t in total:
        index += 1
        if aim in t.values():
            for key, value in t.items():
                data_switch[value] = key
            print("當前資料:\n部門\t姓名\t年齡\t手機\n------------------------------\
----------")
            for value in t.values():
                print(value, end="\t")
            print()
            break
    if len(data_switch) == 0:
        print("查無此人")
    else:
        field = (int)(input("\n1. 修改部門\n2. 修改姓名\n3. 修改年齡\n4. 修改手機\n請\
選擇要修改的欄位: "))
        if field == 1:
            total[index]["department"] = input("請輸入新的部門: ")
        elif field == 2:
            total[index]["name"] = input("請輸入新的姓名: ")
        elif field == 3:
            total[index]["age"] = input("請輸入新的年齡: ")
        else:
            total[index]["phone"] = input("請輸入新的手機: ")
        print("\n--- 更新後的資料 ---\n部門\t姓名\t年齡\t手機\n-----------------------\
-----------------")
        for value in total[index].values():
            print(value, end="\t")
        print()


def delete():
    '''delete someone info'''
    include = 0
    if len(total) == 0:
        print("無資料可刪除")
    else:
        aim = input("請輸入要刪除的姓名: ")
        for t in total:
            if aim in t.values():
                include = 1
                if input("確定要刪除 "+aim+" 的資料嗎? (y/n): ") == "y":
                    total.remove(t)
                    print(aim+" 的資料已刪除。")
                break
        if include == 0:
            print("查無此人")


def display():
    '''show all info'''
    if len(total) == 0:
        print("目前沒有任何資料")
    else:
        print("部門\t姓名\t年齡\t手機\n----------------------------------------")
        for t in total:
            for value in t.values():
                print(value, end="\t")
            print()


total = []
select = 0
while select != 6:
    print("\n--- 人事資料管理系統 ---\n1. 新增資料\n2. 查詢資料\n3. 修改資料\n\
4. 刪除資料\n5. 顯示所有資料\n6. 退出系統\n------------------------")
    select = (int)(input("請選擇功能: "))
    mode()
