class Phone:
    send_message = 0
    receive_message = 0
    calling = 0
    def __init__(self):
        self.send_message = Phone.send_message
        self.receive_message = Phone.receive_message
        self.calling = Phone.calling
    def send(self):
        self.send_message += 1 
        print("正在发短信")
    def receive(self):
        self.receive_message += 1
        print("收到短信")
    def call(self):
        if self.calling == 0:
            self.calling = 1
            print("打电话")
        elif self.calling == 1:
            print("正在打电话，请稍后再打")
    def Hang_up(self):
        if self.calling == 1:
            self.calling = 0
            print("电话打完了")
        elif self.calling == 0:
            print("没有正在打的电话")
A = Phone()
A.send()
A.receive()
A.call()
A.call()
A.Hang_up()
A.call()
A.Hang_up()
A.Hang_up()