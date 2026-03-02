# we create a function that receives a name of the file (cwords)
# inside the file we will search for the longest word that starts with "c"
# we must open the file to read it
# we remove punctuation so it is more clear
# we split each line into words
# we check every word
# if it starts with "c", we compare its length with the current longest word
# if it is longer, we update the variable
# finally we return the longest word found


def longest_cword(file):
    """
    Returns the longest word that starts with 'c'
    """
    longest = ""
    with open(file, "r") as f:
        for line in f:
            line = line.replace(",", "")
            line = line.replace(".", "")
            line = line.replace(";", "")
            line = line.replace(":", "")

            words = line.split()

            for word in words:
                if word.startswith("c"):
                    if len(word) > len(longest):
                        longest = word

    return longest

print(longest_cword("cwords"))