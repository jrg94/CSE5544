with open("E:\\Projects\\CSE5544\\assignment04\\data\\testGHZ400.data") as f:
    with open("E:\\Projects\\CSE5544\\assignment04\\data\\testGHZ400clean.data", "w") as out:
        for line in f:
            print(",".join(line.split()), file=out)
