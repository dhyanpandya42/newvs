def read_file(file_path):
   
    
    with open(file_path, 'r') as file:
        return file.readlines()

def count_lines(lines):
    "counts line"
    return len(lines)

def wordscount(lines):
    "splits the lines into words"
    words = lines.split()
    return len(words)

def vowelConsonantsCount(lines):
    """Count the number of vowels and consonants."""
    vowels = "aeiouAEIOU"
    countvowel = 0
    countConsonant = 0
    for char in lines:
        ".isalpha is an inbuild function to check alphabets"
        if char.isalpha():
            if char in vowels:
                countvowel += 1
            else:
                countConsonant += 1
    return countvowel, countConsonant

def non_letterCount(lines):
    """Counts non-letters."""
    countNonLetter = 0
    for char in lines:
        "we used 'not' is alpha ,coz all the character that are not alphabets will go into it,including digits and spaces"
        if not char.isalpha():
            countNonLetter += 1
    return countNonLetter





def main(file_path):
    lines = read_file(file_path)
    
    
    vowelsTotal = 0
    consonantsTotal = 0
    totalNonletters = 0
    total_words = 0
    
    for line in lines:
       
        vowelsPerLine, consonantsPerLine = vowelConsonantsCount(line)
        
        vowelsTotal += vowelsPerLine
        consonantsTotal += consonantsPerLine
        totalNonletters += non_letterCount(line)
        total_words += wordscount(line)
    print()
    print(f"Vowel count: {vowelsTotal}")
    print(f"Consonant count: {consonantsTotal}")
    print(f"Non-letter character count: {totalNonletters}")
    print(f"Line count: {count_lines(lines)}")
    print(f"Word count: {total_words}")


file_path = r'C:\Users\dpandya3\Documents\python\newvs\lab66.txt'  
main(file_path)