stack={"top":-1,"dizi":[]}

def bosMu():
    return stack["top"]==-1

def push(eleman):
    stack["top"]+=1
    stack["dizi"].append(eleman)
    print(f"{eleman} stacke eklendi!")

def pop():
    if bosMu():
        print("Eleman silinemedi stack bos")
        return
    eleman=stack["dizi"][stack["top"]]
    stack["dizi"].pop()
    stack["top"]-=1
    print(f"{eleman} stackten silindi! ")

def sonElemanNe():
    if bosMu():return 1
    return stack["dizi"][stack["top"]]

def tumStack():
    if bosMu():
        print("\nElemanlar bastırılamadı stack bos\n")
        return
    kapasite=stack["top"]
    for i in range(kapasite,-1,-1):
        deger=stack["dizi"][i]
        print(f"| {i}. - {deger}.|")
    print("-"*25)



push(15)
tumStack()
push(25)
tumStack()
pop()
tumStack()
pop()
tumStack()
push(26)
tumStack()
pop()
tumStack()
push(10)
push(20)
push(30)
push(40)
push(50)
tumStack()
