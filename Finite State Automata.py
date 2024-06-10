class FSA:
    def __init__(se):
        se.transitions = {'q0': {'a': 'q1', 'b': 'q0'},
                            'q1': {'a': 'q1', 'b': 'q2'},
                            'q2': {'a': 'q1', 'b': 'q0'}}
        se.start = 'q0'
        se.accept = 'q2'
    def process(se, s):
        state = se.start
        for char in s:
            state = se.transitions[state].get(char, None)
            if state is None:
                return False
        return state == se.accept
fsa = FSA()
for s in ['ab', 'aab', 'bba', 'aabb', 'abab','abb']:
    print(f"String '{s}' accepted: {fsa.process(s)}")
