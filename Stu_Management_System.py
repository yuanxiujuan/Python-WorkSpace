# coding=utf-8
class StuManagementSystem(object):
    def __init__(self):
        self.students = []
        self.__menu()

    def __menu(self):
        print("-" * 30)
        print("| 1 添加学生或者添加课程     |")
        print("| 2 删除学生及对应的课程     |")
        print("| 3 修改学生的基本信息       |")
        print("| 4 查询信息                 |")
        print("| 5 退出学生管理系统         |")
        print("-" * 30)

    def addStudent(self, newstudent):
        self.students.append(newstudent)

    def delStudent(self,stu):
        i=0
        for student in self.students:
            if stu.get_id() == student.get_id():
                del self.students[i]
            i+=1

    def select(self):
        print("------------所有学生的基本信息------------")
        print("id    name  sex   age")
        for stu in self.students:
            id=stu.get_id()
            name=stu.get_name()
            sex=stu.get_sex()
            age=stu.get_age()
            print("%-6s%-6s%-6s%-6s"%(id,name,sex,age)),
            stu.get_course()

    def is_has(self, newid):
        for stu in self.students:
            if stu.get_id() == newid:
                return stu
        return 0


class Student(object):
    def __init__(self, id, name, sex, age):
        self.id = id
        self.name = name
        self.sex = sex
        self.age = age
        self.course = {}

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age

    def get_course(self):
        for i,j in self.course.items():
            print(" %s:%d"%(i,j)),
        print

    def addCourseScore(self, course, score):
        self.course[course] = score

    def modifyStudent(self):
        name=raw_input("请输入修改后的名字：")
        sex=raw_input("请输入修改后的性别：")
        age=raw_input("请输入修改后的年龄：")
        self.name=name
        self.sex=sex
        self.age=age

stu_management_system = StuManagementSystem()

while True:
    choice = int(input("请输入操作序号："))

    if choice == 1:
        print("添加学生请输入a  添加课程请输入b")
        add_choice = raw_input("请输入您的选择：")
        if add_choice == "a":

            id = raw_input("请输入您的学号：")
            name = raw_input("请输入您的姓名：")
            sex = raw_input("请输入您的性别：")
            age = int(raw_input("请输入您的年龄："))

            is_has = stu_management_system.is_has(id)
            while is_has != 0:
                id = raw_input("已有该学号的学生！请重新输入学号：")
                is_has = stu_management_system.is_has(id)

            new_stu = Student(id, name, sex, age)
            stu_management_system.addStudent(new_stu)

        elif add_choice == "b":
            id = raw_input("请给课程指定学生的学号：")
            is_has = stu_management_system.is_has(id)
            if is_has != 0:

                courName = raw_input("请输入课程名：")
                score = int(raw_input("请输入分数："))
                is_has.addCourseScore(courName, score)
                while True:
                    choice = raw_input("若不想继续添加课程，请输入q Q,若想继续添加，请输入y Y:")
                    if choice == "y" or choice == "Y":
                        courName = raw_input("请输入课程名：")
                        score = int(raw_input("请输入分数："))
                        is_has.addCourseScore(courName, score)
                    elif choice == "q" or choice == "Q":
                        break
            elif is_has == 0:
                print("该学号的学生不存在！")
        else:
            print("没有该选项！")

    elif choice == 2:
        id=raw_input("请输入您要删除的学生的学号：")
        is_has=stu_management_system.is_has(id)
        if is_has !=0:
            stu_management_system.delStudent(is_has)
        elif is_has == 0:
            print("没有该学号的学生！")


    elif choice == 3:
        id=raw_input("请输入您要修改的学生的学号：")
        is_has = stu_management_system.is_has(id)
        if is_has != 0:
            is_has.modifyStudent()
        elif is_has == 0:
            print("没有该学号的学生！")

    elif choice ==4:
        stu_management_system.select()

    elif choice == 5:
        break