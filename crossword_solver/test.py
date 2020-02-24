def test():
    t1 = TestSol("anagram", "test 1", 0.8)
    t2 = TestSol("hidden", "test 2", 0.7)
    return [t1, t2]

class TestSol:
    def __init__(self, t, text, score):
        self.t = t
        self.score = score
        self.text = text
    
    def get_text(self):
        return self.text
    
    def get_score(self):
        return self.score

    def get_type(self):
        return self.t
    
    def __str__(self):
        return "{} - confidence: {}".format(self.text, self.score)