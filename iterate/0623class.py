print("2인용 끝말잇기 게임을 시작합니다")

A = input("player1의 이름을 입력하세요 : ")
B = input("player2의 이름을 입력하세요 : ")

Player = [A,B]

print("세글자 단어를 입력하세요")

while True:
    word1 = input(A + ":")
    if (len(word1) == 3):   
        break    
    else:
        print("세글자 단어를 다시 입력하세요")
    
i = 1

while True:
    word2 = input(Player[i] + ":")
    if (len(word2) == 3) & (word2[0] == word1[-1]):
        word1 = word2
        if (i == 0):
            i = i + 1
        else :
            i = i - 1
    else:
        print(Player[i] + "님이 졌습니다.")
        break
    
print("게임이 끝났습니다.")


# GIT 변경사항 CHECK
# GITHUB에서 수정 중입니다.
# 한번더 수정합니다.
