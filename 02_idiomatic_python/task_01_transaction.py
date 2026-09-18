def total_by_user(transactions):
    tbu = {}
    for t in transactions: 
        tbu[t[0]] = tbu.get(t[0], 0) + t[2]
    return tbu

def format_scores(names, scores):
    return [
        f"{i}. {name}: {score}"
        for i, (name, score) in enumerate(zip(names, scores), start=1)
    ] 

def validate_users(users):
    return all(u["age"] for u in users) and any(u["active"] for u in users)

def analyze_users(users):
    total = 0
    adults = 0
    active = 0
    all_adults = True
    any_inactive = False

    for i, (name, age, is_active) in enumerate(users, start=1):
        total += 1

        if age >= 18:
            adults += 1
        else:
            all_adults = False

        if is_active:
            active += 1
        else:
            any_inactive = True

    return {
        "total": total,
        "adults": adults,
        "active": active,
        "all_adults": all_adults,
        "any_inactive": any_inactive,
    }

def chunked(iterable, size): 

    iterator = iter(iterable) # next works just for iterable type
    counter = 0
    chunk = []

    while True:
        try: 
            chunk.append(next(iterator))
            counter += 1
        except StopIteration:
            if chunk:
                yield chunk 
            break
        if counter == size: 
            yield chunk
            chunk = []
            counter = 0

def main():
    # 1. Lista
    print(list(chunked(range(10), 3)))

    # 2. Chunk più grande dell'iterable
    print(list(chunked(range(5), 10)))

    # 3. Dimensione esatta
    print(list(chunked(range(6), 3)))

    # 4. Generator
    numbers = (x for x in range(7))
    print(list(chunked(numbers, 2)))

    # 5. Stringa
    print(list(chunked("abcdef", 2)))


if __name__ == "__main__":
    main()
