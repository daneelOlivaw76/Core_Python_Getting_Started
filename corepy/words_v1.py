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

<<<<<<< HEAD:corepy/words_v1.py
#print(__name__)

=======
>>>>>>> 882a83e9176e7184487b4c736b3fdfd1a9772f61:corepy/words_func.py
if __name__ == '__main__':
    fetch_words()
