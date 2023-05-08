import json


#def main():
#    file_pointer = open("news.txt", "r")
#    var = file_pointer.readlines() 
#    file_pointer2 = open("subs.json", "r")
#    print(file_pointer2)
#    data = json.load(file_pointer2)
#    better = open("betternews.txt", "a")
#    
#    for _ in range(len(var)):
#        for i in range(len(var[_].split())):
#            if (var[_].split())[i] in data.keys():
#                better.write(str(data.keys()))
#            else:
#                better.write((var[_].split())[i] + " ")
#        better.write("\n")
#    file_pointer.close()
#    file_pointer2.close()
#    better.close()
#
#main()



def main2():
    text = open("news.txt", "r").read().lower()
    sub_fptr = open("subs.json", "r")
    subs = json.load(sub_fptr)

    #use one list to modify another list
    #which list should you loop through?

    for k, v in subs.items():
        text = text.replace(k, v)
    fptr = open("betternews.txt", "w")
    fptr.write(text)
    fptr.close()

main2()