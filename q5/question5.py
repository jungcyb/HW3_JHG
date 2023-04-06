def reverse_words(str) :
    words = str.split(" ")
    res = ""
    for word in words :
        res = word + " " + res
    return res

input1 = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
input2 = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"

if __name__ == "__main__" :
    print("input1 : \n", reverse_words(input1), sep="")
    print("input2 : \n", reverse_words(input2), sep="")
