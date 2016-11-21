# demo.py
#_*_coding:utf-8 _*_

class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score

#bart=Student('Jack',80)

#print bart.name
#print bart.score
    def print_score(std):
        print '%s: %s' %(std.__name,std.__score)
        #Zreturn None


    def get_grade(self):
        if self.__score>=90:
            return 'A'
        elif self.__score>=60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0<=score<=100:
            self.__score = score
        else:
            raise ValueError('bad score')



bart=Student('Jack',80)

print bart.get_name()
print bart.get_score()
bart.set_score(100)
print bart.get_score()

print bart._Student__name


