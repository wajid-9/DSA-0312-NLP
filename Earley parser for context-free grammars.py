from collections import defaultdict, namedtuple
grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N']],
    'VP': [['V', 'NP']],
    'Det': [['the']],
    'N': [['cat'], ['dog']],
    'V': [['chased'], ['saw']]
}
State = namedtuple('State', ['lhs', 'rhs', 'dot', 'start'])
class EarleyParser:
    def __init__(self, grammar):
        self.grammar = grammar
    def parse(self, text):
        words = text.split()
        chart = defaultdict(list)
        chart[0].append(State('γ', ['S'], 0, 0))
        for i in range(len(words) + 1):
            for state in chart[i]:
                if self.dot_at_end(state):
                    self.complete(chart, state, i)
                elif self.next_symbol(state) in self.grammar:
                    self.predict(chart, state, i)
                elif i < len(words):
                    self.scan(chart, state, i, words[i])
        return any(state.lhs == 'γ' and self.dot_at_end(state) and state.start == 0 for state in chart[len(words)])
    def dot_at_end(self, state):
        return state.dot == len(state.rhs)
    def next_symbol(self, state):
        return None if self.dot_at_end(state) else state.rhs[state.dot]
    def predict(self, chart, state, i):
        for rhs in self.grammar[self.next_symbol(state)]:
            chart[i].append(State(self.next_symbol(state), rhs, 0, i))
    def scan(self, chart, state, i, word):
        if self.next_symbol(state) == word:
            chart[i + 1].append(State(state.lhs, state.rhs, state.dot + 1, state.start))
    def complete(self, chart, state, i):
        for s in chart[state.start]:
            if self.next_symbol(s) == state.lhs:
                chart[i].append(State(s.lhs, s.rhs, s.dot + 1, s.start))
parser = EarleyParser(grammar)
text = "the cat chased the dog"
result = parser.parse(text)
print(f"Parsing result for '{text}': {result}")
