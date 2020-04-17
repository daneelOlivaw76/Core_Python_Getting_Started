from urllib.request import urlopen
def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()

    string = '\n'
    for word in story_words:
        string += word + ' '
    string = string.rstrip() + '.'
    print(string)

if __name__ == __main__:
    fetch_words()
