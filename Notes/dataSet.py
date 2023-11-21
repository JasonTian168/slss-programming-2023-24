with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    print(f.readline())

with open("./data_example.csv", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        print(line.split(","))

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    chicken_count = 0
    for line in f:
        if "Chicken Adobo" in f:
            chicken_count += 1

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    num_Count = 0
    for line in f:
        if line[0] == "A":
            num_Count += 1

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    numCount = 0
    for line in f:
        if "Guangzhou" in f:
            numCount += 1
            