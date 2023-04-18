import sys


def monoton(lista:list[str])->bool:
    for i in range(1,len(lista)):
        if len(lista[i-1])> len(lista[i]):
            return False
    return True

def main():
    if monoton(sys.argv[1:]):
        print("YES")
    else:
        print("NO")

if __name__=="__main__":
    main()