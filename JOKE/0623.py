# ##########for문을 이용해서 구구단 출력하기 ############### 
# for i in range(2,10): #2~9까지의 범위만큼 i가 반복합니다.
#     for j in range(2,10): #i가 2일때 j는 2,3,4,5,6,7,8,9 i가 3일때 j는 2,3,4,5,6,7,8,9 이런식으로 반복합니다.
    
#         print(i,"X",j,"=",i*j) #,로 구분해서 for문이 돌때마다 변하는 i와 j그리고 그 곱하기 기호와 = 기호로 이어줍니다.
# ##########한번만 답할수있는 구구단 게임 ##################
# import random #python에서 제공해주는random함수입니다.
# # random.randrange(2,10) <- 이렇게 2~9까지의 랜덤한 숫자를 보여줍니다.
# a = random.randrange(2,10)
# b = random.randrange(2,10)
# answer = a * b   #실제 정답 값을 answer에다가 넣어서 비교해주려 하고 있습니다.
# input_value = int(input( str(a) + " X " + str(b) + " = "))   # 입력 받은 값을 int로 바꿔서 정답과 비교합니다
# #그런데 이때 input의 도움말을 보여줄껀데 a와 b는 현재 int이므로 문자열과 + 로 연결해줄수 없습니다.
# #따라서 int인 a와 b을 str()로 둘러싼다음 string으로 형변환을 해주고 +로 문자와 연결해 도움말을 보여 주도록합시다.
# if (answer == input_value): #실제 곱한 값이랑 사용자가 입력한 input_value랑 같으면 정답을 print해줍니다.
#     print("정답입니다")
# else:
#     print("오답입니다.")
    
############# 함수를 이용한 여러번 대답하는 구구단게임 ###############
import random 
def gugudan():  #반복적으로 사용할 예정이므로 함수화 시켜주었습니다.
    a = random.randrange(2,10)
    b = random.randrange(2,10)
    
    answer = a * b   #실제 정답 값을 answer에다가 넣어서 비교해주려 하고 있습니다.
    
    input_value = int(input( str(a) + " X " + str(b) + " = "))   # 입력 받은 값을 int로 바꿔서 정답과 비교합니다
    #그런데 이때 input의 도움말을 보여줄껀데 a와 b는 현재 int이므로 문자열과 + 로 연결해줄수 없습니다.
    #따라서 int인 a와 b을 str()로 둘러싼다음 string으로 형변환을 해주고 +로 문자와 연결해 도움말을 보여 주도록합시다.
    
    if (answer == input_value):  
        print("정답입니다")
        
        return True#함수가 실행되면 print() 동작 뿐만아니라 return으로 True, False를 반환하여 반복문을 컨트롤 해줍니다.
    else:
        print("오답입니다")
        
        return False
        
while True: #항상 반복문이 돌아가도록 True로 설정해놓습니다.
    gogo = gugudan() #gugudan 함수를 실행하고 return 되는 True값 혹은 False값을 gogo 라는 변수에 담아놓습니다.
    
    if gogo == False: #gugudan이 실행되고 만약 오답을 입력하면 return값이 False이므로 gogo에는 False값이 담길 것이고
                      #그렇게 되면 break로 가장 가까운 반복문인 while문을 탈출하게되고 구구단을 끝내게 됩니다.
        break