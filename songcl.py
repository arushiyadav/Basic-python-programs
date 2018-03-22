class song():
    def __init__(self,lyrics):
        song.lyrics = lyrics
    def sing_a_song(self):                 
        for line in self.lyrics:
            print(line)
hbd = song(["hb to u","may god bless u"])
hbd.sing_a_song()
twinkle = song(["twinkle twinkle","little stars"])
twinkle.sing_a_song()
class name():
    def __init__(self,name):
        self.name = name
    def hi(self):
        print("hello, my name is",self.name)
obj = name("arushi")
obj.hi()