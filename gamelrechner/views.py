from django.shortcuts import render

# Create your views here.
def form(request):
    return render(request, 'form.html')

def result(request):
    punktzahl = 0

    height = int(request.POST['height'])
    weight = int(request.POST['weight'])
    iq = int(request.POST['iq'])
    hair = int(request.POST['hair'])
    beard = int(request.POST['beard'])
    age = int(request.POST['age'])

    print(getPzAge(age))
    #punktzahl += getPzAge(age)
    
    print(getPzHeight(height))
    punktzahl += getPzHeight(height)*2

    print(getPzBmi(height, weight))
    punktzahl += getPzBmi(height, weight)*2

    print(getPzBfp(request.POST['radios']))
    punktzahl += getPzBfp(request.POST['radios'])*2

    print(getPzIq(iq))
    punktzahl += getPzIq(iq)*2

    print(getPzHair(hair))
    punktzahl += getPzHair(hair)

    print(getPzBeard(beard))
    punktzahl += getPzBeard(beard)





    return render(request, 'result.html', {"punktzahl": punktzahl})

def getPzAge(age):
    if age > 60:
        return 1
    elif age > 50:
        return 2
    elif age > 40:
        return 3
    elif age > 30 or age < 18:
        return 4
    elif 18 <= age <= 30:
        return 5


def getPzHeight(height):
    if height <= 154 or height >= 225:
        return 1
    elif height <= 164 or height >= 215:
        return 2
    elif height <= 174 or height >= 205:
        return 3
    elif height <= 184 or height >= 195:
        return 4
    elif height <= 194:
        return 5
    
def getPzBmi(height, weight):
    bmi = weight / (height/100) **2
    if 40 <= bmi:
        return 1
    elif bmi < 18.5 or 35 < bmi < 40:
        return 2
    elif 18.5 <= bmi < 25:
        return 4
    elif 25 <= bmi <= 35:
        return 5
    
def getPzBfp(bpf):
    if bpf == '5':
        return 1
    elif bpf == '4':
        return 2
    elif bpf == '1' or bpf == '3':
        return 4
    elif bpf == '2':
        return 5
    
def getPzIq(iq):
    if iq < 70:
        return 0
    elif iq < 85:
        return 1
    elif iq < 100:
        return 2
    elif iq < 115:
        return 3
    elif iq < 130:
        return 4
    elif 130 <= iq:
        return 5
    
def getPzHair(hair):
    if hair == 1:
        return 5
    elif hair == 2:
        return 3
    elif hair == 3:
        return 1

def getPzBeard(beard):
    if beard == 1:
        return 3
