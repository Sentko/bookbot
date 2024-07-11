def main():
    book_title = input(f"""
What is the book's title ?
(PS : only works if you write 'frankenstein',
but it still should be case insensitive...?)
""").lower()
    def sort_on(item):
        return item[1]
     
    word_count = 0
    file_contents = ''
    unique_character_count = {}
    sorted_count = []    
    #######################################################
    
    with open(f"books/{book_title}.txt") as f: #1) Read book_title.txt and
        file_contents = f.read()               #   store it in file_contents                  
    
    #######################################################
    
    words = file_contents.lower().split() #2) counts words
    for i in words:
        word_count += 1

    #######################################################
    
    
    for i in file_contents.lower(): #3) counts unique chars
        if i.isalpha():           
            if i in unique_character_count:
                unique_character_count[i] += 1
            else:
                unique_character_count[i] = 1
    
    ########################################################
    
    sorted_count = sorted(unique_character_count.items(), reverse=True, key=sort_on) #4) Sorting
    print(f"""
--- Begin report of books/frankenstein.txt ---
{word_count} words found in frankenstein.txt


""")    
    for char, count in sorted_count:
        print(f"'{char} has been found {count} times in the text.'")
    print("--- End report ---")
        
    ########################################################
    
        


if __name__ == '__main__':
    main()