def main() :
    print("******Reverse Word******")
    print()
    print("***First Input String is ***")
    input_string1 = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
    print(input_string1)
    print()
    temp_string1 = input_string1.split()
    final_string1 = ""
    length1 = len(temp_string1)
    
    print("***Result of First is*** ")
    for i in range(length1) :
        final_string1 = final_string1 + temp_string1[length1-i-1] + " "
    print(final_string1)
    print()
    print("***Second Input String is ***")
    input_string2 = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"
    print(input_string2)
    print()
    temp_string2 = input_string2.split()
    final_string2 = ""
    length2 = len(temp_string2)
    
    print("***Result of Second is*** ")
    for i in range(length2) :
        final_string2 = final_string2 + temp_string2[length2-i-1] + " "
    print(final_string2)
    
if __name__ == "__main__":
    main()
