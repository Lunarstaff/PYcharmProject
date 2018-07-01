#class-test.py

# Dog类
class Dog():
    """
    小狗类
    """
    def __init__(self, name, age):
        """
        初始化
        :param name: name
        :param age: age
        :return:
        """
        self.name = name
        self.age = age

    def sit(self):
        """
        小狗蹲下
        :return:
        """
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """
        小狗打滚
        :return:
        """
        print(self.name.title() + " rolled over.")

#Car 类
class Car():
    """
    汽车类
    """
    def __init__(self, make, model, year):
        """
        初始化
        :param make:
        :param model:
        :param year:
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23 # 里程计，默认值为23

    def get_descriptive_name(self):
        """返回描述信息"""
        long_name = str(self.year) + ' ' + self.make.title() + ' ' + self.model.title()
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage): # 更新里程表读数
        """
        将里程表读数设置为指定的值，
        禁止将里程表里读数往回调
        :param mileage:
        :return:
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You Can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    """电池对象"""
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        """打印电池信息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

class Electric_car(Car):
    """电动车 从Car类继承"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year) #初始化父类的属性
        # self.battery_size = 70 # 电动车自己特有的属性，电池默认值为70
        self.battery = Battery() # 电动车有一个电池对象


# #创建一个表示特定小狗的实例：
# my_dog = Dog('huahua', 6)
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")
# my_dog.sit()
#
# #创建一个我的新车实例
# my_new_car = Car('audi', 'a4' , 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

my_tesla = Electric_car('China', 'X86', 2018)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery() #调用电动车对象中电池对象的方法