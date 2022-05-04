def run():
    a = "Marvin"
    otro = a[:0] + 'm' + a[1:]

    print(otro)


if __name__ == '__main__':
    run()