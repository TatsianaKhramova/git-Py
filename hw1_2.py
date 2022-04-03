
numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
sorted_numbers = []
def main():
    for i in range(len(numbers)):
        try:
            numbers[i] = int(numbers[i])
            sorted_numbers.append(numbers[i])
        except (ValueError,TypeError):
            pass
    print(numbers)
    print(min(sorted_numbers), max(sorted_numbers))


if __name__ == '__main__':
    main()