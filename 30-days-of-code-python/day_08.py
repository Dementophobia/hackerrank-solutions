i = int(input())
phonebook = dict()

for _ in range(i):
    entry = list(input().split())
    phonebook[entry[0]] = entry[1]

while True:
    # We don't know in advance how many queries will come.
    # Therefore, we have to 'try'.
    try:
        query = input()
    except:
        break

    if query in phonebook:
        print(f"{query}={phonebook[query]}")
    else:
        print("Not found")