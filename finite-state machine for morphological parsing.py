class PluralizerFSM:
    def __init__(self):
        self.rules = [
            (lambda word: word.endswith(('s', 'x', 'z', 'ch', 'sh')), lambda word: word + 'es'),
            (lambda word: word.endswith('y') and word[-2] not in 'aeiou', lambda word: word[:-1] + 'ies'),
            (lambda word: True, lambda word: word + 's')
        ]

    def generate_plural(self, word):
        for condition, action in self.rules:
            if condition(word):
                return action(word)
pluralizer = PluralizerFSM()
test_words = ['cat', 'dog', 'bus', 'box', 'buzz', 'church', 'dish', 'baby', 'boy']
for word in test_words:
    plural = pluralizer.generate_plural(word)
    print(f"Singular: {word}, Plural: {plural}")
