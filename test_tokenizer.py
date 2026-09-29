import re 
from tokenizer import KenjiTokenizer

def build_vocab(text):
    tokens = re.split(r'([,.:;?_!"()\']|--|\s)', text)
    tokens = sorted({t.strip() for t in tokens if t.strip()}) # strip whitespace
    tokens.append("<|unk|>")
    tokens.append("<|endoftext|>") 
    return {tok: i for i, tok in enumerate(tokens)} # enumerate always yields (index, item)

# def test_roundtrip():
#     text = "Hello, do you like tea? I do."
#     tok = KenjiTokenizer(build_vocab(text))
#     assert tok.decode(tok.encode(text)) == text

def test_endoftext_is_one_token():
    text = "Hello, do you like tea? I do."
    vocab = build_vocab(text)
    vocabs_tokenizer = KenjiTokenizer(vocab)

    prompt = "I dont like tea <|endoftext|> Hello"
    ids = vocabs_tokenizer.encode(prompt)

    assert len(ids) == 6
    assert ids[4] == vocab["<|endoftext|>"]

if __name__ == "__main__":
    test_endoftext_is_one_token()
    print("pass")