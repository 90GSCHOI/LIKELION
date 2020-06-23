# import random
# import time

# Lunch = ["된짱찌개", "피자", "제육볶음", "짜장면"]

# while True:
#     print(Lunch)
#     item = input("음식을 추가해주세요(없으면 q) :")
#     if(item == "q"):
#         break
#     else:
#         Lunch.append(item)
    
    
# print("현재 리스트는", Lunch)


# while True:
#     print(Lunch)
#     item = input("빼고 싶은 음식이 있으신가요(없으면 q) :")
#     if(item == "q"):
#         break
#     else:
#         set_Lunch = set(Lunch)
#         set_Lunch = set_Lunch - set([item])
#         Lunch = list(set_Lunch)

# print("최종 리스트는", Lunch)
# print("이 중에서 오늘의 점심을 선택을 합니다")
# print("시작!!!")
# print("5")
# time.sleep(1)
# print("4")
# time.sleep(1)
# print("3")
# time.sleep(1)
# print("2")
# time.sleep(1)
# print("1")
# time.sleep(1)

# print("오늘의 점심은", random.choice(Lunch))

total_list = []

while True:
    question = input("질문을 입력해주셈(그만하고 싶으면 q) : ")
    if (question == "q"):
        print("*"*50)
        break
    else:
        total_list.append({"질문" : question, "답변" :""})

for i in total_list:
    print(i["질문"])
    answer = input("답변을 입력하세요 : ")
    i["답변"] = answer

print(total_list)
    
