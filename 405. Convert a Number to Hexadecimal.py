map_hex={
        1:'1',
        2:'2',
        3:'3',
        4:'4',
        5:'5',
        6:'6',
        7:'7',
        8:'8',
        9:'9',
        10:'a',
        11:'b',
        12:'c',
        13:'d',
        14:'e',
        15:'f'
    }
def convert(x):
    return map_hex[x]

def tohex(num):
    r_hex=[]
    while((num//16)!=0):
        h=num%16
        r_hex.append(convert(h))
        num=num//16

    h=num%16
    r_hex.append(convert(h))
    r_hex.reverse()
    return "".join(r_hex)


def tobinary(num):
    r_bin=[]
    while((num//2)!=0):
        b=num%2
        r_bin.append(str(b))
        num=num//2
    b=num%2
    r_bin.append(str(b))
    len_bin=len(r_bin)
    count=32-len_bin
    r_bin.extend(count*['0'])
    #r_bin.reverse()
    return r_bin

def flip(x):
    if x=='0':
        return '1'
    else:
        return '0'

def add_binary(l1):
    complent=['1']
    complent.extend(31*['0'])
    result=[]
    carry=0
    for i in range(len(l1)):
        if l1[i]=='0' and complent[i]=='0':
            if carry==0:
                result.append('0')
            else:
                result.append('1')
                carry=0
        elif l1[i]=='0' and complent[i]=='1':
            if carry==0:
                result.append('1')
            else:
                result.append('0')
                carry=1

        elif l1[i]=='1' and complent[i]=='0':
            if carry==0:
                result.append('1')
            else:
                result.append('0')
                carry=1
        
        elif l1[i]=='1' and complent[i]=='1':
            if carry==0:
                result.append('0')
                carry=1
            else:
                result.append('1')
                carry=1


    return result

def to_decimal(l):
    l=list(map(int,l))
    r=[]
    sum=0
    for i in range(len(l)):
        p=i-4*(i//4)
        sum+=(l[i]*(2**p))

        if (i+1)%4==0:
            r.append(sum)
            sum=0

    r=[convert(item) for item in r]
    r.reverse()
    return "".join(r)





if __name__=="__main__":
    num=-1
    if num<0:
        tobin=tobinary(abs(num))
        #print(tobin)

        flip_bin=[flip(x) for x in tobin]

        #print(flip_bin)

        r=add_binary(flip_bin)
        #print(r)

        result=to_decimal(r)
        print(result)
    elif num>0:
        print(tohex(num))
    else:
        print("0")
    

