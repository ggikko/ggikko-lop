import re

text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
regex = re.compile("에러 1033")
mo = regex.search(text)
if mo is not None:
    print(mo.group)

text = "ㄱ문사항이 있으면 032-232-3245 으로 연락주시기 바랍니다. 2문22의사항ㄴ"

regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchobj = regex.search(text)
phonenumber = matchobj.group()
print(phonenumber)

regex = re.compile('있으면')
sub = re.sub('있으면', '', text)
print(sub)
# print(regex)
# test3 = regex.search(text)
# print(test3)
# print(test3.group())
