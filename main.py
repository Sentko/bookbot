def main():
    def sort_on(item):
        return item(1)
     
    word_count = 0
    file_contents = ''
    unique_character_count = {}    
    #######################################################
    
    with open("books/frankenstein.txt") as f: #Read-Prints frankenstein.txt
        file_contents = f.read()              
        print(file_contents)                  
    
    #######################################################
    
    words = file_contents.lower().split()
    for i in words:
        word_count += 1
    print(word_count)

    #######################################################
    
    
    for i in file_contents.lower().isalpha():
        if i.isalpha():           
            if i in unique_character_count:
                unique_character_count[i] += 1
            else:
                unique_character_count[i] = 1
    return unique_character_count
    
    ########################################################
    
    sorted_counts = sorted(unique_character_count.items(), key=sort_on, reverse=True)
    print(sorted_counts)
    
        


if __name__ == '__main__':
    main()