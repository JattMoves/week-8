from collections import defaultdict


class MarkovText(object):

    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = None  # you'll need to build this

    def get_term_dict(self):
        tokens = self.corpus.split()
        terms = defaultdict(list)

        for current, following in zip(tokens, tokens[1:]):
            terms[current].append(following)

        self.term_dict = dict(terms)
        return self.term_dict

    def generate(self, seed_term=None, term_count=15):
        if self.term_dict is None:
            self.get_term_dict()

        if seed_term is not None and seed_term not in self.corpus.split():
            raise ValueError(f"Seed term {seed_term!r} is not in the corpus")

        if term_count <= 0:
            return ""

        if not self.term_dict:
            raise ValueError("Cannot generate text from an empty corpus")

        current = (
            np.random.choice(list(self.term_dict.keys()))
            if seed_term is None
            else seed_term
        )
        generated = [current]

        for _ in range(term_count - 1):
            next_terms = self.term_dict.get(current)
            if not next_terms:
                break

            current = np.random.choice(next_terms)
            generated.append(current)

        return " ".join(generated)