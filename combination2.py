def combination(n):
    if n==1:
        return ["()"]
    else :
        item="()"
        result=combination(n-1)
        tuple_concat=[]
        for r in result:
            tuple_concat.append(item+r)
            for i in range(len(r)):
                tuple_concat.append(r[0:i]+item+r[i:])
            tuple_concat.append(r+item)
        return tuple_concat
    


if __name__=="__main__":
    n=int(input())
    all_parts=combination(n)
    parts=list(set(all_parts))
    print(parts)
    print(len(parts))
