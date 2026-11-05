def increase_3(number):
    result = number + 3
    return result


def list_avg(numlist):
    for number in numlist:
        sum = sum + number
        avg = sum/len(numlist)

    return avg


def sub_number(number1, number2):
    result = number1 - number2
    return result


def max(numlist):
    result = max(numlist)
    return result


def is_even_or_odd(num):
    if num % 2 == 0 :
        print(num, "is even")
    else:
        print(num, "is odd")

def list_add(new_num, new_list):
    if new_num in new_list:
        print("이미 있는 원소")
    else:
        new_list = new_num + [new_num]
        print("원소를 추가하였습니다")


# ----------------------------------------------------------------

# 연습문제 1.
def average(number1, number2):
    result = (number1 + number2)
    return average

# 2. 결과값 예측 1,2,3
# 3. 정의, 호출

# 4. 
def print_greeting(n):
    for count in range(n):
        print("Hello World")


# 5. 
def sum(n):
    result = 0
    for count in range(n):
        result = result + count
        return result

# 6. 
def add(a,b):
    return a+b

print(add(3,5))

# 
def rectangle(a, b):
    result = (a+b)*2
    return result

print(rectangle(3,6))

# 
def max_score(score):
    max_num = score[0]

    for num in score:
        if num > score:
            max_num = num

    print(f"최고 점수는 {num}입니다.")


# 
def tempo_change():
    temp = 0

    print("현재 템포는 0입니다. 템포 조정은 0부터 5까지 가능합니다.")

    change = int(input("조정하고자 하는 만큼 크기를 입력 : "))

    if 0 <= change <= 5 :
        temp = temp + change
        print(f"조정한 후 템포는 {temp}입니다.")

    else:
        print("0부터 5까지 입력하세요")

tempo_change()

# 
def volume_up():
    volme = 3

    print("현재 음량은 3입니다.")

    change = int(input("증가시킬 만큼의 음량을 입력: "))

    volme = volme + change
    print(f"증가 후 음량은 {volme}입니다. ")


volume_up()

# 
def 출근여부():
    name = input("이름을 입력하세요: ")

    if name == "suzu" :
        print("출근 완료했습니다.")

    else:
        print("출근이 불가합니다.")

출근여부()

# 
def train_ticket():
    city = input("춘천 / 부산 / 대구 / 수원 중 한곳을 입력하세요: ")

    if city == "춘천":
        price = 5000
    elif city == "부산":
        price = 30000
    elif city == "대구":
        price = 20000
    elif city == "수원":
        price = 10000
    else:
        print("잘못된 도시 이름입니다.")
        return

    print(city, "까지의 금액은", price, "원 입니다.")

train_ticket()


# 리팩토링

def train_ticket(city):
    price = {
        "춘천":5000,
        "부산":30000,
        "대구":20000,
        "수원":10000
    }

    fare = price.get(city)

    if fare is None:
        return "잘못된 도시입니다."

    return (f"{city}까지 금액은 {fare}입니다.")

city = input("도시입력: ")
print(train_ticket(city))

#

def facotrial(x):
    result = 1

    for i in range(1, x+1):
        result = result * i

    return result

# 11장 함수의 활용 예제 11-1

score = [90, 80, 70, 60, 50]

sum = 0 
max_score = 0
average = 0

for num in score:
    sum += num

    average = sum / len(sum)

    if max_score < num:
        max_score = num

    if average >= 60 :
        message = "pass"
    else:
        message = "false"

print("average = ", int(average) , "max_score = ", max_score)
print("you",message , "the class")


# 예제 11-2

def list_avg(numlist):
    sum , average = 0, 0
    for num in numlist:
        sum = sum + num

        average = sum / len(num)

    return average


# 실습 11-1 

def longest(a,b,c):

    result = a

    if len(b) > len(result):
        result = b

    if len(c) > len(result):
        result = c

    return result



def shortlest(a,b,c):

    result = a

    if len(b) < len(result):
        result = b

    if len(c) < len(result):
        result = c

    return result

# 실습 11-2

def len_word(wordlist):
    sum = 0
    for word in wordlist:
        sum += len(word)

    return sum

# 실습 11-3

def calavg(numlist):
    result = 0

    for num in numlist:
        result += num


    return result / len(numlist)


def passFail(numlist):

    avg = calavg(numlist)

    return "Pass" if avg >= 60 else "Fail"

print(passFail([30,40,50,60,70]))

#-----------------------------------------------------------
# 실습 11-4
def max_score(score_list):

    max_num = score_list[0]

    for score in score_list:
        if score > max_num:
            max_num = score

    return max_num

# ----------------------------------
# 실습 11-5
def gap_score(score_list):
    max_score = score_list[0]
    min_score = score_list[0]

    for score in score_list:
        if score > max_score:
            max_score = score

        elif score < min_score:
            min_score = score

    return max_score - min_score

# ------------------------------------

# 실습 11-6
def change_temp(temperature):

    result = ((9/5) * temperature + 32)

    return result

temperature = input("섭씨 온도 입력: ")
print(change_temp(temperature))


# 실습 11-7
# meter 를 입력받아 yard , feet 변환
# 함수 정의 chagne_meter(meter)
# 소수점이므로 float()형변환

def change_meter(meter):

    feet = float(meter / 0.305)
    yard = float(meter * 1.0936)

    return (f"{meter}는 {yard},{feet}입니다.")

meter = float(input("meter를 입력: "))
print(change_meter(meter))

# 실습 11-8


def cal_area(bottom, height):
    area = float(0.5 * bottom * height)
    return area

bottom = int(input("정수 입력하세요"))
height = int(input("정수 입력하세요"))
print(cal_area(bottom, height))


# 실습 11-9

def cal_time_data(time):
    
    if time < 24*60*60:
        hour = time // 3600
        minute = (time % 3600) // 60
        sec = time % 60

        print(f"{hour}시 {minute}분 {sec}초 이다.")
    else:
        print("입력 시간이 하루를 초과합니다.")


time = input("시간을 입력하세요")
cal_time_data(time)

# 실습 11-10

def cal_productPrice(totalPrice):
    return totalPrice / 1.1


def cal_tax(totalPrice):
    return totalPrice - cal_productPrice(totalPrice)

totalPrice = int(input("입력하세요: "))

productPrice = cal_productPrice(totalPrice)
tax = cal_tax(totalPrice)

print(f"제품가격은 {productPrice}원, 부가가치세 {tax}원입니다. ")


# 실습 11-11

passward = input("비밀번호를 입력하세요. ")

def checkPw(passward):
    if len(passward) >= 9:
        return "Good"

    elif len(passward) >= 5:
        return "Normal"

    else:
        return "Bad"

print("Your password:", checkPw(passward))


# 실습 11-12

def periodDiscount(contractPrice, period):
    discount = contractPrice * period

    if discount <= 6 :
        return contractPrice * 0

    elif 6 <= discount < 12:
        return contractPrice * 0.1

    else:
        return contractPrice * 0.2


def cardDiscount(contractPrice, cardCode):
    card_discount = contractPrice * cardCode

    if card_discount == 11:
        return contractPrice * 0.05

    elif card_discount == 12:
        return contractPrice * 0.08

    elif card_discount == 13:
        return contractPrice * 0.12

contractPrice = int(input("계약 금액 입력: "))
period = int(input("사용 개월 수 입력: "))
cardCode = int(input("카드 코드 입력: "))

finalPrice = (contractPrice - periodDiscount(contractPrice,period)-
              cardDiscount(contractPrice,cardCode))

print("최종금액은:",{finalPrice},"입니다")

# 실습 11-13 
# 내려가라는 함수
# 올라가라는 함수

def getupfloor(floor):
    return floor + 1

def getdownfloor(floor):
    return floor -1

inputLocation = input("사용자가 가고 싶은 층을 입력하세요: ")
nowLocation = input("사용자가 현재 있는 층을 입력하세요: ")

# 다른 층 입력했을 때 1~6층 입력하라는 반복문
if not 1<= inputLocation <= 6 or not 1<= nowLocation <= 6 or inputLocation == nowLocation :
    print("다른 층 (1~6)을 눌러주세요 ")

else:
    print(f"현재 층은 {nowLocation} 입니다.")


    while nowLocation != inputLocation:
        if nowLocation <= inputLocation:
            nowLocation = getupfloor(nowLocation)
        else:
            nowLocation = getdownfloor(nowLocation)


        print(f"현재충은 {nowLocation} 입니다.")

    print(f"{inputLocation}층에 도착했습니다. 안녕히가세요. ")


# 실습 11-14 계산기 프로그램

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return abs(num1 - num2)

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0 :
        return "0으로 나눌 수 없음."
    return num1 / num2


print("===== 게산기 =====")

while True:
    menu = input("1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 5.종료 ")

    if menu == "5":
        break

    if menu not in ("1","2","3","4"):
        print("메뉴를 다시 선택해주세요.")
        continue

    print("정수 2개를 입력해주세요")
    num1 = float(input())
    num2 = float(input())

    if menu == "1":
        result = add(num1 + num2)

    elif menu == "2":
        result = abs(num1 - num2)

    elif menu == "3":
        result = num1 * num2

    elif menu == "4":
        result = num1 / num2


    print("결과", result)

# 실습 11-15

def circum(side1, side2):
    return (side1 + side2) * 2

def area(side1, side2):
    return side1 * side2

while True:

    menu = input("1.둘레 2.넓이 3.종료")

    if menu == "3":
        break

    if menu not in ("1","2"):
        print("메뉴를 다시선택해주세요.")
        continue


    print("변 2개 입력하세요")

    side1 = float(input())
    side2 = float(input())


    if side1 <= 0 or side2 <=0:
        print("양수로 입력해주세요")
        continue

    if menu == 1:
        print("둘레는",{circum},"입니다.")
    else:
        print("넓이는",{area},"입니다.")


# 실습 11-16 점수의 평균, 최고, 최저점 구하기

def avg_score(numlist):

    total = 0

    for score in numlist:
        total += score
    return total / len(numlist)


def high_score(numlist):

    highest = numlist[0]

    for score in numlist:
        if score > highest:
            highest = score
    return highest

    

def low_score(numlist):
    lowest = numlist[0]

    for score in numlist:
        if score < lowest:
            score = lowest
    return lowest

scores = [95, 90, 45, 10, 80, 100]


print("학생들의 점수는 95, 90, 45, 10, 80, 100 점입니다.")

menu = input("1.평균 2.최고점 3.최저점 ")

if menu == "1":
    print("1.평균: ", {avg_score(scores)})

elif menu == "2":
    print("2.최고점: ", {max(scores)})

elif menu == "3":
    print("3.최저점: ", {min(scores)})

else:
    print("메뉴를 닫시 클릭해주세요")


# 실습 11-17

def volume(now_vol, num):
    result = now_vol + num
    if result < 0:
        return 0
    if result > 100:
        return 100
    return result

def eco(now_eco, num):
    result = now_eco + num
    if result < -3:
        return -3
    if result > 3:
        return 3
    return result

def tempo(now_tem, num):
    result =  now_tem + num
    if result < -5:
        return -5
    if result > 5:
        return 5
    return result

now_vol = 60
now_eco = 0
now_tem = 0

print("=== 노래방 기계 조절 프로그램 ===")

menu = input("1.음량 2.에코 3.템포")

if menu == "1":
    print("음량 조절은 0부터 100까지 가능합니다. 현재 음량은",{now_vol}," 입니다.")
    num = int(input("조절 입력: "))
    now_vol = volume(now_vol, num)
    print("조절 후 음량은 ", now_vol," 입니다.")

elif menu == "2":
    print("에코 조절은 -3부터 3까지 가능합니다. 현재 에코는", now_eco," 입니다.")
    num = int(input("조절 입력: "))
    now_eco = eco(now_eco, num)
    print("조절 후 에코는 ", now_eco, " 입니다.")


elif menu =="3":
    print("템포 조절은 -5부터 5까지 가능합니다. 현재 템포는 ", now_tem, " 입니다.")
    num = int(input("조절 입력"))
    now_tem = tempo(now_tem, num)
    print("조절 후 템포는 ", now_tem, " 입니다.")

else:
    print("메뉴를 다시 입력해주세요")


# 실습 11-18

def channel(now_cha, num):
    result = now_cha + num



def volume(now_vol, num):
    result = now_vol + num


now_cha = 5
now_vol = 4

while True:
    menu = input("1.채널 2.음량 3.종료")

    if menu == "3":
        break

    if menu not in {"1","2"}:
        print("메뉴룰 다시 선택해주세요.")
        continue

    num = int(input("바꾸고 싶은 정도 입력: "))

    if menu == "1":
        now_cha = channel(now_cha, num)
        print("현재 채널은 ", now_cha)

    else:
        now_vol = volume(now_vol, num)
        print("현재 볼룸은 ", now_vol)



# 실습 11-19 기차표 예매

# 기차 예메 프로그램 >> 1. 목적지 선택 2. 열차 종류 선택 3. 죄석인지 입석인지 선택  / 금액 모두 다름 / 총 금액 출력하는 함수

def objection(o):

    fares = {
        "춘천" : 5000,
        "부산" : 30000,
        "대구" : 20000,
        "수원" : 10000
    }

    return fares.get(o)


def train(t):

    fares = {
        "KTX" : 20000,
        "새마을호": 10000,
        "무궁화호": 8000
    }

    return fares.get(t)

def ud(s):
    if s == "좌석":
        return 0
    elif s == "입석":
        return 2000
    return None


def cal_payment(a, b, c):
    payment = a + b - c
    print(payment,"원")


목적지 = input("목적지를 입력하세요(춘천,부산,대구,수원) ")
열차종류 = input("열차 종류를 입력하세요(KTX,무궁화호,새마을호)")
입좌여부 = input("좌석 / 입석 입력하세요 ")

a = objection(목적지)
b = train(열차종류)
c = ud(입좌여부)

if a is None or b is None or c in None:
    print("항목을 다시 선택해주세요.")

else:
    cal_payment(a,b,c)



# 실습 11-20

def Coffee(c):
    menu = {
        "Americano" : 3900,
        "Cafe mocha": 4500,
        "Cafe Latte" : 4800,
        "Green Tea Latte": 5000    
    }
    return Coffee.get(c)


def size(s):
    sizes = {
        "G" : 1000,
        "R" : 500,
        "S" : 0
    }
    return sizes.get(s)


def price(a, b):
    total = a + b
    print("총 금액은 ", {total})


print("Welcome to Harry Cafe")

coffee = input("1. Americano 2. Cafe mocha 3. Cafe Latte 4. Green Tea Latte / 커피명을 입력해주세요. ")
sizes = input("G(grande), R(regulr), S(short): ")

a = Coffee(coffee)
b = price(sizes)

if a is None or b is None:
    print("메뉴, 사이즈를 다시 선택해주세요.")

else:
    price(a, b)






