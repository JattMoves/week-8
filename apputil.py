from collections import defaultdict
import numpy as np

class MarkovText(object):
    """ A class that generates text based on a Markov chain model."""
    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = None  

    def get_term_dict(self):
        tokens = self.corpus.split()
        terms = defaultdict(list)

        for current, following in zip(tokens, tokens[1:]):
            terms[current].append(following)

        self.term_dict = dict(terms)
        return self.term_dict

    def generate(self, seed_term=None, term_count=15):
        """_summary_

        Args:
            seed_term (_type_, optional): _description_. Defaults to None.
            term_count (int, optional): _description_. Defaults to 15.

        Raises:
            ValueError: _description_
            ValueError: _description_

        Returns:
            _type_: _description_
        """
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

            if next_terms:
                current = np.random.choice(next_terms)
            else:
                current = np.random.choice(list(self.term_dict.keys()))

            generated.append(current)

        return " ".join(generated)