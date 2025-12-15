def change(money):
    # write your code here
    count = 0
    count += m // 10
    money %= 10
    count += m // 5
    money %= 5
    count += money

    return money


if __name__ == '__main__':
    m = int(input())
    print(change(m))
