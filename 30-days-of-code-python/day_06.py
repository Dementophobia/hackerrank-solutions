for _ in range(int(input())):
    s = input()

    even = [s[i] for i in range(0, len(s), 2)]
    odd  = [s[i] for i in range(1, len(s), 2)]
    
    print(f"{''.join(even)} {''.join(odd)}")