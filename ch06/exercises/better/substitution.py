import json


def main():
    file_pointer = open("news.txt", "r")
    var = file_pointer.readlines() 
    file_pointer2 = open("subs.json", "r")
    print(file_pointer2)
    data = json.load(file_pointer2)
    better = open("betternews.txt", "a")
    
    for _ in range(len(var)):
        for i in range(len(var[_].split())):
            if (var[_].split())[i] in data.keys():
                better.write(str(data.keys()))
            else:
                better.write((var[_].split())[i] + " ")
        better.write("\n")
    file_pointer.close()
    file_pointer2.close()
    better.close()

main()
