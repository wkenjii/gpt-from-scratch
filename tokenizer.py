import re

class KenjiTokenizer:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_"!()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [
            item if item in self.str_to_int else "<|unk|>" # then check the item here and replace the empty ones with <|unk|>
            for item in preprocessed # we only want the words, thats why we looped thro the preprocessed
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        print(type(ids), ids)
        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[s] for s in ids])
        text = re.sub(r'\s+([,.:;?!"\()])', r'\1', text)
        return text