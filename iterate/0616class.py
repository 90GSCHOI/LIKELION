mydict = {1:'hello'}
mydict2=dict()
mydict22={}
mydict3 = {'이름':'장치훈','나이':12,'특징':['하나','둘']}
mydict3['추가']='내용'
print("*"*50,type(mydict2),type(mydict22))
print(mydict)
print(mydict[1])
print(mydict3)
print(mydict3.keys())
print(mydict3.values())
print(mydict3.items())
print(mydict3['이름'])
print(mydict3.get('이름'))
print(mydict3.get('성별','입력을 안했습니다'))

print("키가 딕셔너리 안에 있나?", '키' in mydict3)
print(mydict2)
