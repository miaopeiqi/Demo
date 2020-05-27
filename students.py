data = {}
num = int(input('pleast enter the num of students:'))
Subjects = ('Math','History','Phics')

for i in range(num):
    name = input('please enter student\'s name:')
    marks = []
    for x in Subjects:
        marks.append(float(input('please enter the mark of {}:'.format(x))))    
    data[name] = marks

for x,y in data.items():
    total = sum(y)
    print("{}\'s total mark is:{}".format(x,total))
    if total < 120:
        print(x,'failed:(')
    else:
        print(x,'passed:)')