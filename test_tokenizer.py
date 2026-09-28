import re 
from tokenizer import KenjiTokenizer

def build_vocab(text):
    tokens = re.split(r'([,.:;?_!"()\']|--|\s)', text)
    tokens = sorted({t.strip() for t in tokens if t.strip()}) # strip whitespace
    tokens.append("<|unk|>") 
    return {tok: i for i, tok in enumerate(tokens)} # enumerate always yields (index, item)

def test_roundtrip():
    text = "Hello, do you like tea? I do."
    tok = KenjiTokenizer(build_vocab(text))
    assert tok.decode(tok.encode(text)) == text

if __name__ == "__main__":
    test_roundtrip()
    print("pass")