
from translator import translate


def demo_check_grammar(text: str, rules: list[str]) -> None:

    trees = translate(text)
    for tree in trees:
        print(f'Sentence: {tree.get_sentence()}')
        feedbacks = tree.check_selected_rules(rules)
        for feedback in feedbacks:
            print(feedback)
    print("=====")


def example() -> None:
    """Print out (to the console) an example of grammar checking using
    demo_check_grammar.
    """
    sentence = "The foxes jumps over"
    # 2 errors in sentence:
    # 1) foxes + jumps
    # 2) no end punctuation
    demo_check_grammar(sentence, ["*"])


if __name__ == '__main__':
    example()

    import python_ta
    python_ta.check_all(config={
        'max-line-length': 100,
        'disable': [],
        'extra-imports': ['translator'],
        'allowed-io': ['demo_check_grammar'],
        'max-nested-blocks': 4
    })
