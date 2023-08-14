import os


def get_content(filename):
    """Reads the contents of a file and returns it as a string."""
    with open(filename, "r") as f:
        content = f.read()
    return content

def check_file_existence(filename):
    """Checks if a file exists and is readable."""
    if os.path.exists(filename):
        return True
    else:
        return False
      
def get_symbols_count(content):
    """ Finds the letters and numbers used in the specified file."""
    letters_and_numbers = {}
    for line in content:
        for character in line:
            if character.isalpha():
                if character not in letters_and_numbers:
                    letters_and_numbers[character] = 0
                letters_and_numbers[character] += 1
            elif character.isdigit():
                if character not in letters_and_numbers:
                    letters_and_numbers[character] = 0
                letters_and_numbers[character] += 1

    return letters_and_numbers

def get_longest_word(content):
    """Finds the longest word in a string."""
    words = content.split(" ")
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def get_sentences_count(content):
    """Counts the number of sentences in a string."""
    sentences = content.split(".")
    return len(sentences)

def get_text_with_words_reversed(content):
    """Reverses the order of the words in a string."""
    words = content.split(" ")
    reversed_words = []
    for word in words:
        reversed_word = ""
        for i in range(len(word) - 1, -1, -1):
            reversed_word += word[i]
        reversed_words.append(reversed_word)
    return " ".join(reversed_words)

def write_into_file(filename, content):
    """Writes a string into a file."""
    with open(filename, "a") as f:
        f.write(str(content))
    

def main():
    """The main function."""
    filename = "data.txt"
    newFilename = "new_data.txt"
    if not check_file_existence(filename):
        print("File doesn't exist!")
        return

    content = get_content(filename)
    
    if os.path.exists(newFilename):
        os.remove(newFilename)
    
    write_into_file("new_data.txt", "Finds the letters and numbers used in the specified file -" + str(get_symbols_count(content))+ "\n")
    write_into_file("new_data.txt", "Finds the longest word in a string.-" + get_longest_word(content) + "\n")
    write_into_file("new_data.txt", "Counts the number of sentences in a string - " + str(get_sentences_count(content)) + "\n")
    write_into_file("new_data.txt", "Reverses the order of the words in a string - " + get_text_with_words_reversed(content))

main()

 