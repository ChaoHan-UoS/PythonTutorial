class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


def sentence(sentence):
    for word in sentence.split():
        yield word


# my_sentence = Sentence('This is a test')  # The object is iterable but also an iterator.
my_sentence = sentence('This is a test')  # Using a generator

# for word in my_sentence:  # The for loop catches the StopIteration exception for us but doesn't show us that
#     print(word)

print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))