#main()함수 실행코드는 맨 밑에 있습니다!

import csv
from datetime import date,datetime

def do_customize_main(dogInfo, d):

    # infile = open(datafile,'r')
    # doglist = []
    # dogInfo = getData('dog_types.csv')
    # dogResult = []

    #txt 파일 마지막에는 무조건 end 써주기 
    # for line in infile:
    #     if line == "end":
    #         break
    #     temp = line.split(",")
    #     doglist.append(
    #         [int(temp[0]),float(temp[1]),temp[2],float(temp[3]),int(temp[4]),
    #          int(temp[5]),temp[6],int(temp[7]),int(temp[8]),temp[9],temp[10][:-1]])
    # for d in doglist:
    dogInstance = dog(dogInfo,d)
    dogResult = dogInstance.dogmain()
    return dogResult


# petID, age, breedID,   weight, gender, neut  , neutdate, obesity, activity, hi,    taste
# 12,     1,    Poodle,  22.46,    1,    0,     0,           1,        1,   diabetes,chicken
# 15 ,    1,    Poodle,   22.47,   1,    0,      0,          1,        1,   pregnant,salmon
# 17,    5.6,   Poodle,   29.25,  1,     1,    2018-06-03,  1,          1,  0,        None
# 18,     1.2,  Poodle,   29.25,  1,     1,    2018-06-03,  2,          1,   0,      beefs
# self.result["petID"] = self.petID
# self.result["Neutralization"] = self.checkNeut()
# self.result["Age"] = self.getAge()
# self.result["Specification"] = self.checkSpec()
# self.result["Activity"] = self.checkActivity()
# self.result["Activity Calculation"] = self.calActivity()
# self.result["Obesity"] = self.checkObesity()
# self.result["Size"] = self.checkSize()
# self.result["Ingredient Set Number"] = self.ingClassification()
# petID,    neut,    age,     specification,     activity,    activitycalc, obesity,   size,  ingredient set numbrt

#헤더:값 딕셔너리 형태로 받기

def getData(file):
    with open(file, 'r', encoding='utf-8') as f:
        doginfo = []
        for row in csv.DictReader(f):
           petID = int(row['id'])
           breed = row['name']
           weight=getWeightTuple(row['weight'])
           life_span=getLifeTuple(row['life_span'])
           doginfo.append([petID,breed,weight,life_span])
    return doginfo

#Starts, Up, From과 같이 단어들 처리하기
#Starts이면 (지정 년도 혹은 무게, None)
#Up이면 (초기시점인 0, 지정 년도 혹은 무게)
#From-to이면 (최소 지정 년도 혹은 무게, 최대 지정 년도 혹은 무게)

def getWeightTuple(r):
    tlist = r.split()
    if "NULL" not in tlist:
        t = (tlist[0],tlist[2])
        if 'Starts' in t:
            t = (round(int(tlist[2])*0.45,1),None)
        elif 'Up' in t:
            t = (0, int(tlist[2])*0.45)
        elif 'From' in t:
            t = (round(int(tlist[1])*0.45,1),round(int(tlist[3])*0.45,1))
        else:
            t = (round(int(tlist[0])*0.45,1),round(int(tlist[2])*0.45,1))
        return t
    
def getLifeTuple(r):
    tlist = r.split()
    if "NULL" not in tlist:
        t = (tlist[0],tlist[2])
        if 'Starts' in t:
            t = (int(tlist[2]),None)
        elif 'Up' in t:
            t = (0, int(tlist[2]))
        elif 'From' in t:
            t = (int(tlist[1]),int(tlist[3]))
        else:
            t = (int(tlist[0]),int(tlist[2]))
        return t


def binary_search_recursive(dogInfo, breed):

    first = 0
    last = len(dogInfo) - 1

    if len(dogInfo) == 0:
        return "There is no such breed in our data base"
    else:
        i = (first + last) // 2
        if breed == dogInfo[i][1]:
            return int(dogInfo[i][0])
        else:
            if dogInfo[i][1] < breed:
                return binary_search_recursive(dogInfo[i+1:], breed)
            else:
                return binary_search_recursive(dogInfo[:i], breed)





class dog():
    
    def __init__(self,info,dlist):
        self.info = info
        self.petID = dlist[0]
        self.age=dlist[1]
        self.breedID=binary_search_recursive(info,dlist[2])
        self.weight=dlist[3]
        self.gender=dlist[4]
        self.neut=dlist[5]
        self.neutdate = dlist[6]
        self.obesity=dlist[7]
        self.activity=dlist[8]
        self.hi=dlist[9]
        self.taste=dlist[10]
        self.ageClassified = ""
        self.neutClassified = ""
        self.sizeClassified = ""
        self.obesityClassified =""
        self.activityClassified = ""
        self.result = {}
        self.ingNum = ""
        self.weight_error = 0

    def checkObesity(self):
        #0,1,2(뚱뚱)로 받음
        avgWeight = ((int)(self.info[self.breedID-1][2][0])+(int)(self.info[self.breedID-1][2][1]))/2
        deviation = self.info[self.breedID-1][2][1] - avgWeight
        subVal=abs(self.weight - avgWeight)
        if subVal > deviation*1.3:
            print("The value of weight is excessed our expectation.")
            self.weight_error = 1
        if self.weight- avgWeight>=0:
            if subVal < deviation*0.6:
                self.obesity += 2
            else:
                self.obesity += 4
        else:
            if subVal < deviation*0.6:
                self.obesity += 2

        if self.obesity > 4:
            self.obesityClassified = "Overweight"
        elif self.obesity >= 2:
            self.obesityClassified = "Normal"
        else:
            self.obesityClassified = "Underweight"

        return(self.obesityClassified)
                
    def checkSize(self):
        avgWeight = ((int)(self.info[self.breedID-1][2][0])+(int)(self.info[self.breedID-1][2][1]))/2
        if round(avgWeight,2) <= 3.5:
            self.sizeClassified = "Toy"
        elif round(avgWeight,2) <= 7:
            self.sizeClassified = "Small"
        elif round(avgWeight,2) <= 15:
            self.sizeClassified = "Medium"
        elif round(avgWeight,2) <= 30:
            self.sizeClassified = "Large"
        else:
            self.sizeClassified = "Extra Large"

        return(self.sizeClassified)

    def checkActivity(self):
    #0,1,2 로 받음
        if self.activity == 2:
            self.activityClassified = "Very Active"
        elif self.activity == 1:
            self.activityClassified = "Normal"
        else:
            self.sizeClassified = "Less Active"
        return self.activityClassified

    def calActivity(self): ## Let's calculate her or his activity degree!!
        if self.getAge()== 'Puppy' or self.checkSpec() == 'pregnant': ## [] number is an assumption
            return 130
        elif self.checkSpec() == 'lactation':
            return 145
        elif self.neut == True:
            return 112
        elif self.checkObesity() == "Overweight":
            return 98
        elif self.checkActivity() == "Less Active":
            return 95
        elif self.getAge() == 'Old' and self.checkActivity() == "Very Active":
            return 105
        elif self.checkActivity == "Very Active":
            return 140
        else:
            return 126
        
            
    def checkNeut(self):
        now = datetime.today()
        now = date(now.year, now.month, now.day)
        tp_neut = ("Not Neutralized", "Neutralized Beforehand", "Recently Neutralized")
        if self.neutdate != "0":
            ndate= date(int(self.neutdate[0:4]), int(self.neutdate[5:7]), int(self.neutdate[8:]))
            term = now - ndate
            term = term.days
            
            if term < 14:
                self.neutClassified = tp_neut[2]
            else:
                self.neutClassified = tp_neut[1]
        else:
            self.neutClassified = tp_neut[0]
        return (self.neutClassified)


    def getAge(self):
        tp_age = ("Puppy", "Adult", "Old")
        avgLifespan = (self.info[(self.breedID)-1][3][0]+self.info[(self.breedID)-1][3][1])/2
        stdLifespan = avgLifespan * 0.6
        
        if self.age<0 or self.age>25:
            print("Wrong Value")
        elif self.age<=1:
            self.ageClassified = tp_age[0]
        elif self.age>1 and self.age<stdLifespan:
            self.ageClassified = tp_age[1]
        else:
            self.ageClassified = tp_age[2]
        return(self.ageClassified)
                                      
    def checkSpec(self):
        if self.hi is "0":
            self.hi = "No specification"
        return (self.hi)

    def ingClassification(self):
        ingredientSet = {'111':1,'112':2,'113':3,'121':4,'122':5,
                 '123':6,'131':7,'132':8,'133':9,'211':10,
                 '212':11,'213':12,'221':13,'222':14,'223':15,
                 '231':16,'232':17,'233':18,'311':19,'312':20,
                 '313':21,'321':22,'322':23,'323':24,'331':25,
                 '332':26,'333':27,'411':28,'412':29,'413':30,
                 '421':31,'422':32,'423':33,'431':34,'432':35,
                 '433':36,'511':37,'512':38,'513':39,'521':40,
                 '522':41,'523':42,'531':43,'532':44,'533':45}
        
        if self.sizeClassified == "Toy":
            self.ingNum += "1"
        elif self.sizeClassified == "Small":
            self.ingNum += "2"
        elif self.sizeClassified == "Medium":
            self.ingNum += "3"
        elif self.sizeClassified == "Large":
            self.ingNum += "4"
        else:
            self.ingNum +="5"

        if self.obesityClassified == "Overweight":
            self.ingNum +="3"
        elif self.obesityClassified == "Normal":
            self.ingNum +="2"
        elif self.obesityClassified == "Underweight":
            self.ingNum +="1"

        if self.ageClassified == "Old":
            self.ingNum += "3"
        elif self.ageClassified == "Adult":
            self.ingNum += "2"
        if self.ageClassified == "Puppy":
            self.ingNum += "1"

        return(int(ingredientSet[self.ingNum]))

            
        

    def printClass(self):
        print("petID: ", self.petID)
        print("breedID: ", self.breedID)
        print("classified: ", self.classified)
        print("taste: ", self.taste)
        print("specification: ", self.hi)

    def dogmain(self):
        self.result["petID"] = self.petID
        self.result["Neutralization"]= self.checkNeut()
        self.result["Age"]= self.getAge()
        self.result["Specification"] = self.checkSpec()
        self.result["Activity"] = self.checkActivity()
        self.result["Activity Calculation"] = self.calActivity()
        self.result["Obesity"] = self.checkObesity()
        self.result["Size"]=self.checkSize()
        self.result["Ingredient Set Number"] = self.ingClassification()
        self.result["error_weight"] = self.weight_error
        return (self.result)



# main("doginput (2).txt")
