from datetime import datetime

# 班主任录入学生成绩

class Person:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

class Student(Person):
  count = 0
  def __init__(self, name, age, gender):
    super().__init__(name, age, gender)
    Student.count += 1
    # 学生ID
    self.stu_id = f'{datetime.now().year}{Student.count:03d}'
    # 成绩集合
    self.scores = {}

  def add_score(self, subject, score):
    self.scores[subject] = score

  def calcu_avg(self):
    if self.scores:
      return sum(self.scores.values()) / len(self.scores)
    else:
      return 0
    
  # 魔法方法
  def __str__(self):
    return f'{self.name}({self.age}-{self.gender})，成绩：{self.scores}，平均分:{self.calcu_avg():.1f}'
    

# 班主任
class Manager:
  def __init__(self):
    self.stu_list = []

  def add_student(self):
    name = input('请输入学生姓名：')
    age = int(input('请输入学生年龄：'))
    gender = input('请输入学生性别：')

    stu = Student(name, age, gender)
    self.stu_list.append(stu)
    print(f'学生{stu.name}添加成功，学号为：{stu.stu_id}')

  def del_student(self):
    stu_id = input('请输入要删除的学生学号：')
    for stu in self.stu_list:
      if stu.stu_id == stu_id:
        self.stu_list.remove(stu)
        print(f'学生{stu.name}删除成功')
        return
    print('未找到该学生')

  def show_all_student(self):
    if self.stu_list:
      for stu in self.stu_list:
        print(stu)

  # 给指定学生设置成绩
  def set_score(self):
      sid = input('请输入学号：')
      # 遍历stu_list列表
      for stu in self.stu_list:
          # 如果当前学生学号，与输入的sid相等
          if stu.stu_id == sid:
              # 输入成绩字符串，格式为：学科-分数，学科-分数
              score_str = input('清输入成绩（学科-分数，学科-分数）')
              # 将输入的多个成绩，按照逗号拆分，形成成绩列表
              score_list = score_str.replace('，', ',').split(',')
              # 循环成绩列表，依次添加成绩
              for item in score_list:
                  # 获取科目与成绩
                  subject, score = item.split('-')
                  subject = subject.strip()
                  score = float(score.strip())
                  # 调用add_score方法，添加科目，成绩
                  stu.add_score(subject, score)
              print('添加成功！')
              # 结束循环，同时结束set_score函数
              return
      # 若程序能执行到此处，证明在stu_list中没有找到与sid对应的学生
      print('学号有误！')

  def run(self):
     while True:
        print('************学生管理************')
        print('1. 添加学生')
        print('2. 删除学生')
        print('3. 查看所有学生')
        print('4. 录入成绩')
        print('5. 退出')

        chocie = input('请输入操作编号：')
        if chocie == '1':
            self.add_student()
        elif chocie == '2':
            self.del_student()
        elif chocie == '3':
            self.show_all_student()
        elif chocie == '4':
            self.set_score()
        elif chocie == '5':
            print('再见！')
            break
        else:
            print('输入有误！')

m1 = Manager()
m1.run()