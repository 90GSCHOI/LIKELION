# a = int(input("숫자를 입력해주세요! : "))

# if (a > 10):
#     print("a는 10보다 큽니다")
# elif (a == 5):
#     print("a는 5입니다")
# else:
#     print("a는 10보다 작군요")

# if (a > 5):
#     print("a는 5보다 큽니다.")
# if (a > 0):
#     print("a는 자연수 입니다.")
    
    
# if (a%2 ==0):
#     print("a는 짝수 입니다.", a%2)
# else :
#     print("a는 홀수 입니다", a%2)

# if (a>0):
#     print("a는 양수입니다")
#     if (a%2 == 0):
#         print("a는 짝수입니다")
#     else:
#         print("a는 홀수입니다")
# else:
#     print("a는 음수입니다")

# for i in [1,2,3,4,5]:
#     print ("i의 값은:", i)

# while a < 5:
#     print ("a의 값은:", a)
#     a = a+1

    
    
# for i in range(1000):
#     print(i)


# tmp_str = "오늘은 날씨가 좋은 토요일 오후입니다."
# for i in range(len(tmp_str)):
#     print(tmp_str[i], "의 인덱스는 :", i)

# a = input("글자수를 세고 싶은 글을 쓰세요:")
# for i in range(len(a)):
#     ()
# print("글자수는:",i+1)

# for i in range(100):
#     print(i)

# def forfunction(a):
#     for i in range(a):
#         print(i)

# forfunction(5)
# print("*" *100)
# forfunction(10)


# def hellofunction(a):
#     if a%2 == 0:
#         for i in range(a):
#             print("yes"*i)
#     else:
#         for i in range(a):
#             print("no"*i)
        
# a = int(input("숫자를 쓰세요:"))
# hellofunction(a)

# for i in [1,2,3,4]:
#     print(i)
#     if i == 3:
#         break

# class NSS:
#     body = "강화합금"
    
#     def run(self):
#         print("나는 달립니다")

print("구구단")
for i in range(10):
    if i == 0:
        continue
    else:
        print(i,"단")
        for x in range(10):
            if x != 0:
                a = x * i
                print(i,"*",x,"=",a)
    

        