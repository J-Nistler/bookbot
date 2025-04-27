from stats import count_words, count_letters, sort_results

filepath = "books/frankenstein.txt"

def get_book_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_results (word_count, sorted_results):
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {filepath}...")   
    print ("----------- Word Count ----------")
    print (f"Found {word_count} total words")
    print ("--------- Character Count -------")
    for letter in sorted_results:
        print(f"{letter.get("char")}: {letter.get("num")}")
    print ("============= END ===============")
    return

def main ():
    results = sort_results(count_letters(get_book_text(filepath)))
    wordcount = count_words(get_book_text(filepath))
    print_results(wordcount, results)
    return


main ()