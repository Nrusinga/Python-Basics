class Human:
    def __init__(self,name,occupation):
        self.name=name
        self.occupation=occupation


    def do_work(self):
        if(self.occupation=="actor"):
            print(self.name, "does movies")
        elif(self.occupation=="tennis player"):
            print(self.name, "plays tennis")

    def speaks(self):
        print(self.name, "says how are you")

tom=Human("tom","actor")
tom.do_work()
tom.speaks()
