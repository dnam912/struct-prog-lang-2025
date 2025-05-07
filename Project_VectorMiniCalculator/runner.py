import tokenizer
import parser
import evaluator
import sys

def run(text):
    tokens = tokenizer.tokenize(text)

    # for t in tokens:
    # print(t)

    ast = parser.parse(tokens)
    evaluator.evaluate(ast, {}) # dnam - EXTENDED THE CODE FOR RUNNING THE PROJECT

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1],"r") as f:
            source = f.read()
        run(source)


