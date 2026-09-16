def pipeline(items, *functions):
    for item in items: 
        value = item
        for function in functions:
            value = function(value) 
        yield value  # it's similar to return, but the function doesnt stop after the yield
def main():
    result = pipeline(
        range(5),
        lambda x: x * 2,
        lambda x: x + 1,
    )

    print(list(result))

    result = pipeline(
        (x for x in range(5)),
        lambda x: x ** 2,
    )

    print(list(result))

    result = pipeline(range(5))

    print(list(result))


if __name__ == "__main__":
    main()