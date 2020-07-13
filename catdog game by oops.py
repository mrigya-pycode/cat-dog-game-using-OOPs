import random

class cats_dogs:
    def __init__(self, ran_num):
        self.ran_num = ran_num

    def for_count(self,cat,dog):
        for i in range(len(ran_num)):
            if ran_num[i] == user_ip[i]:
                cat += 1
            else:
                dog += 1
        print("{}:cat,{}:dog".format(cat, dog))

    def for_exit(self):
        if user_ip == "exit":
            exit()

game=True
ran_num = str(random.randint(1000, 9999))
cd=cats_dogs(ran_num)
while True:
    cat=0
    dog=0
    user_ip = str(input("enter the 4 digit number:"))
    cd.for_exit()
    cd.for_count(cat,dog)
    if len(user_ip)>4:
        print("enter valid input please")
    elif cat==4:
        game=False