def seq(k):
    l = k
    s = ''
    n = 1
    while l>0:
        s += n*str(n)
        l -= n
        n += 1
    for i in s[0:k]:
        print(i, end=' ')

if __name__ == "__main__":        
    while True:
        try:
            str = input()
            if str.strip():
                exec(str)
            else:
                break
        except:
            break