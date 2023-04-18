# TODO
import sys
from typing import NamedTuple

Minion=NamedTuple("print_Minion", [
    ("name",str),
    ("hunger",int),
    ("motivation",int),
    ("size", str)
    ])


def from_line(line:str)->Minion:
    tokens=line.strip().split(";")
    return Minion(tokens[0], int(tokens[1]), int(tokens[2]),tokens[3])

def to_line(minion:Minion)->str:
    return f"{minion.name} {minion.hunger} {minion.size}"

##def srt(m:Minion):
      ##return (-m.motivation,m.name)##
def read_minions_from_file1(file_name: str)->list[Minion]:
    minion=[]
    f=open(file_name)
    for line in f:
        minion.append(from_line(line))
    f.close()
    return minion

def read_minions_from_file2(file_name: str)->list[Minion]:
    minion=[]
    with open(file_name) as f:
        for line in f:
            minion.append(from_line(line))
        #f.close()
    return minion

def  order(minions:list[Minion])->list[Minion]:
    ##return sorted(minions, key= srt, )
    return sorted(minions, key= lambda m:(-m.motivation,m.name))

def distinct_motivations(minions: list[Minion])->set[int]:
    ret= set()
    for m in minions:
        ret.add(m.motivation)
    return ret

def distinct_motivations2(minions: list[Minion])->set[int]:
    return {m.motivation for m in minions}

def count_by_sizes(minions: list[Minion])->dict[str,int]:
    ret={}
    for m in minions:
        s=s.size
        if s in ret:
            ret[s]+=1
        else:
            ret[s]=1
    return ret

def count_by_sizes(minions: list[Minion])->dict[str,int]:
    return {s:len([m for m in minions if m.size==s])for s in {x.size for x in minions}}

def group_by_sizes1(minions: list[Minion])->dict[str,list[Minion]]:
    ret = {}
    for m in minions:
        s = s.size
        if s in ret:
            ret[s].append(m)
        else:
            ret[s] = [m]
    return ret

def group_by_sizes2(minions: list[Minion])->dict[str,list[Minion]]:
    ret = {}
    for m in minions:
        s = s.size
        try:
            ret[s]+=1
        except:
            ret[s] = 1
    return ret

def group_by_sizes3(minions: list[Minion])->dict[str,list[Minion]]:
    ret = {}
    for m in minions:
        s = s.size
        ret[s]=ret.get(s, 0)+1
    return ret

def main():

    minions=read_minions_from_file1(sys.argv[1])
    #for line in sys.stdin:
        #minions.append(from_line(line))
    rendezett=order(minions)
    for m in rendezett:
        print(to_line(m))

    dm=distinct_motivations(minions)
    for x in dm:
        print(x)

    cm=count_by_sizes(minions)
    for x in cm:
        print(f'{x}: {cm[x]}')
    for k,v in cm.items():
        print(f'{k}: {v}')

    gm=group_by_sizes1(minions)
    for k,v in gm.items():
        print(k)
        for m in v:
            print(to_line(m))







if __name__=="__main__":
    main()