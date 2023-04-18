import sys
def count_of_odds(numbers: list[int])->int:
    ret=0
    for i in numbers:
        ret+=i%2

        #if i%2==1:
            #ret+=1
    return ret

def main():
     #assert len(sys.argv)>1, "hiányoznak a paraméterek"
    numbers=[]
    if len(sys.argv)>1:
        for i in range(1,len(numbers)):
            numbers.append(int(sys.argv[i]))
    else:
        while True:
            try:

                line=input("Add meg az egészeket: ").strip("")
                tokens=line.split()
                numbers=[]
                for x in tokens:
                    numbers.append(int(x))
            except:
                print("Elgépelted!")
            else:
                break
    print(numbers)
    print(count_of_odds(numbers))


if __name__=="__main__":
    main()