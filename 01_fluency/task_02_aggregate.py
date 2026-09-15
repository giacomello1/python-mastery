def aggregate(items, key):

    aggregate_items = {}
    for item in items: 
        k = key(item)
        if k in aggregate_items:
            aggregate_items[k].append(item)
        else:
            aggregate_items[k] = [item]
    return aggregate_items


def main():
    people = [
        {"name": "Luca", "age": 20},
        {"name": "Anna", "age": 21},
        {"name": "Marco", "age": 20},
        {"name": "Giulia", "age": 21},
    ]

    result = aggregate(people, key=lambda x: x["age"])
    print(result)

    numbers = (x for x in range(10))
    result = aggregate(numbers, key=lambda x: x % 2)
    print(result)

    result = aggregate([], key=lambda x: x)
    print(result)


if __name__ == "__main__":
    main()