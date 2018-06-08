import csv


# 헤더:값 딕셔너리 형태로 받기

def getData(file='dog_types.csv'):
    with open(file, 'r', encoding='utf-8') as f:
        doginfo = []
        for row in csv.DictReader(f):
            petID = int(row['id'])
            breed = row['name']
            weight = getTuple(row['weight'])
            life_span = getTuple(row['life_span'])
            doginfo.append([petID, breed, weight, life_span])
    return doginfo


# Starts, Up, From과 같이 단어들 처리하기
# Starts이면 (지정 년도 혹은 무게, None)
# Up이면 (초기시점인 0, 지정 년도 혹은 무게)
# From-to이면 (최소 지정 년도 혹은 무게, 최대 지정 년도 혹은 무게)

def getTuple(r):
    tlist = r.split()
    if "NULL" not in tlist:
        t = (tlist[0], tlist[2])
        if 'Starts' in t:
            t = (int(tlist[2]), None)
        elif 'Up' in t:
            t = (0, int(tlist[2]))
        elif 'From' in t:
            t = (int(tlist[1]), int(tlist[3]))
        else:
            t = (int(tlist[0]), int(tlist[2]))
        return t


def getAnalysis(doginfo, block):
    test_list = [] #######
    print("Start")

    petID = binary_search_recursive(doginfo, block[1])
    test_list.append(str(petID)) ######
    print(petID)

    averageWeight = ((int)(doginfo[petID - 1][2][0]) + (int)(doginfo[petID - 1][2][1])) / 2
    deviation = doginfo[petID - 1][2][1] - averageWeight
    subVal = abs(block[2] - averageWeight)
    if subVal > deviation * 1.3:
        print("The value of weight is excessed our expectation.")

    obesityPoint = block[3]

    if block[2] - averageWeight >= 0:
        if subVal < deviation * 0.6:
            obesityPoint += 2
        else:
            obesityPoint += 4
    else:
        if subVal < deviation * 0.6:
            obesityPoint += 2

    if obesityPoint >= 4:
        print("pig")
        test_list.append("돼지")   #######
    elif obesityPoint >= 2:
        print("normal")
        test_list.append("정상")  #######
    else:
        print("bones")
        test_list.append("뼈다구")  #######


    if block[4] == 2:
        print("too much")
        test_list.append("운동량 많은편")  #######
    elif block[4] == 1:
        print("normal")
        test_list.append("정상")  #######
    else:
        print("work out!!")
        test_list.append("운동좀 시켜요")  #######

    # return petID
    return test_list


def binary_search_recursive(doginfo, breed):
    first = 0
    last = len(doginfo) - 1

    if len(doginfo) == 0:
        return "There is no such breed in our data base"
    else:
        i = (first + last) // 2
        if breed == doginfo[i][1]:
            return int(doginfo[i][0])
        else:
            if doginfo[i][1] < breed:
                return binary_search_recursive(doginfo[i + 1:], breed)
            else:
                return binary_search_recursive(doginfo[:i], breed)


# a = getData('dog_types.csv')
# getAnalysis(a, ["sarang", "Alaskan Klee Kai", 11, 2, 2])

