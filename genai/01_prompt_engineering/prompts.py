def zero_shot_prompt(question):
    return f"Answer the following question clearly:\n{question}"


def one_shot_prompt(question):
    return f"""
Example:
Question: What is AI?
Answer: AI is the simulation of human intelligence by machines.

Now answer:
Question: {question}
Answer:
"""


def few_shot_prompt(question):
    return f"""
Convert sentences into sentiment labels.

Example 1:
Text: I love this product.
Sentiment: Positive

Example 2:
Text: This is terrible.
Sentiment: Negative

Example 3:
Text: It is okay.
Sentiment: Neutral

Now classify:
Text: {question}
Sentiment:
"""


def main():
    question = "The product is amazing!"

    print("ZERO SHOT:")
    print(zero_shot_prompt(question))

    print("\nONE SHOT:")
    print(one_shot_prompt(question))

    print("\nFEW SHOT:")
    print(few_shot_prompt(question))


if __name__ == "__main__":
    main()