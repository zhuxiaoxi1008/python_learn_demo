class Battery:
    '''初始化电池'''
    def __init__(self, battery_size=70):
        '''初始化电池属性'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''打印一条描述电池容量的消息'''
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
    def get_range(self):
        '''打印一条消息，指出电瓶的续航里程'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)