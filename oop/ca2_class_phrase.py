#!/usr/bin/env python3

in_string = input()
in_string2 = input()

class Phrase:
    def __init__(self, text):
        self.text = text

    def count_words(self):
        words = self.text.split(" ")
        count = 0
        for word in words:
            count += 1
        return count

    def count_characters(self):
        count = 0
        for ch in self.text:
            if ch != " ":
                count += 1
        return count

    def reverse_phrase(self):
        words = self.text.split(" ")
        reversed_words = []
        for i in range(len(words) - 1, -1, -1):
            reversed_words.append(words[i])
        return " ".join(reversed_words)

    def same_word(self):
        words = self.text.split(" ")
        for word in words:
            if word != words[0]:
                return False
        return True

    def __str__(self):
        return f"This phrase has {self.count_words()} words and {self.count_characters()} characters"

    def __eq__(self, other):
        if self.count_words() == other.count_words() and self.count_characters() == other.count_characters():
            return True
        else:
            return False

p1 = Phrase(in_string)
p2 = Phrase(in_string2)
print(p1.reverse_phrase())
print(p1.count_characters())
print(p1.same_word())
print(p1 == p2)
print(p1)