try:
    with open("message.txt", "w+") as file:
        file.write("Hello, Python is Cool! it is a powerful language to Learn.")
        file.seek(0)
        data = file.read()
        print("PowerLearnProject is the Key:")
        print(data)

    with open("massage.txt", "w+") as file:
        file.write("This file should not exist.")
        file.seek(0)
        data = file.read()
        print("I love PowerLearnProject:")
        print(data)

except FileNotFoundError:
    print("Try again later!, invalid file.")
finally:
    print("Clap for yourself; you are on the right path.")
