
# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]

#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])

# class Triangle(Polygon):

#     def __init__(self):_
#         # Polygon.__init__(self,3)
#         super().__init__(3)

#     def findArea(self):
#         a, b, c = self.sides
#         # calculate the semi-perimeter
#         s = (a + b + c) / 2
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print('The area of the triangle is %0.2f' %area)


# t1 = Triangle()
# t1.inputSides()
# t1.dispSides()
# t1.findArea()

class Question():
    num_of_questions = 0
    num_of_correct = 0
    
    
    def __init__(self,  question:str, ans:bool):
        self.question = question
        self.ans = ans
        
        Question.num_of_questions +=1  
        
        
    def take_ans(self):
        print("Expected answers should be Y or Yes or No or N\n")
        while True:
            ans = input(self.question +"\n>")
            if ans.lower() == "y" or ans.lower() == "yes":
                return True
            elif ans.lower() == "no" or ans.lower() == "n":
                return False 
            
    def __check_ans(self, ans):
        if ans == self.ans:
            Question.num_of_correct+=1
        
    def ask(self):
        self.__check_ans(self.take_ans())
        
    @classmethod
    def result(cls):
        return f"You got {Question.num_of_correct} out of {Question.num_of_questions}"


questions = [Question("Python was founded in 1998", False),
            Question("Ronaldo is a terrific player?", True),
            Question("Messi has 10 Ballon d'or", False),
            Question("Django is a python framework", True),
            Question("Julia is used for datascience", True)]

for q in questions:
    q.__check_ans()
    
    
print(Question.result())