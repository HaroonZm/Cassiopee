class dice():
    def __init__(self,men1,men2,men3,men4,men5,men6):
        self.men=[men1,men2,men3,men4,men5,men6]
        self.current_men=1
        self.men_udlr=[5,2,4,3]
        self.move_d=0
        
    def move_dice(self,direction): 
        if direction=="E":
            s=self.men_udlr[2]
            self.men_udlr=[self.men_udlr[0],self.men_udlr[1],
                          7-self.current_men,self.current_men]
            self.current_men=s
        if direction=="N":
            s=self.men_udlr[1]
            self.men_udlr=[self.current_men,7-self.current_men
                           ,self.men_udlr[2],self.men_udlr[3]]
            self.current_men=s
        if direction=="S":
            s=self.men_udlr[0]
            self.men_udlr=[7-self.current_men,self.current_men
                           ,self.men_udlr[2],self.men_udlr[3]]
            self.current_men=s
        if direction=="W":
            s=self.men_udlr[3]
            self.men_udlr=[self.men_udlr[0],self.men_udlr[1]
                           ,self.current_men
                           ,7-self.current_men]
            self.current_men=s
        
    def show_num(self):

        return self.men[self.current_men-1]

m_n=list(map(int,input().split()))
cmd=input()
d=dice(*m_n)
for c in cmd:
    d.move_dice(c)
print(d.show_num())