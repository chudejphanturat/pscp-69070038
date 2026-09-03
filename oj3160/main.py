"""prime"""
def main():
    """prime"""
    prime = 0
    primenum = []
    form,to = map(int ,input().split())
    for i in range(form,to+1):
        if i == 2:
            prime += 1
            primenum.append(i)
        for j in range (2, i):
            if not i % j:
                break
            if j == i-1 or i == 2:
                prime += 1
                primenum.append(i)
    if primenum:
        print(*primenum)
    print(f"Total primes: {prime}")
main()
