def read_int(prompt, min, max):
    try:
        value = int(input(prompt))
        assert value >= min and value <= max
        return value
    except ValueError:
        print("Error: wrong input")
        return read_int(prompt, min, max)
    except AssertionError:
        print("Error: the value is not within permitted range (-10..10)")
        return read_int(prompt, min, max)


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
