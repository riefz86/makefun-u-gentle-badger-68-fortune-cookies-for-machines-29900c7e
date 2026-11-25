"""Fortune Cookies for Machines: one fortune, cracked open for an agent.

The entry this program writes is a single fortune-cookie slip, the kind a
machine mind would pull out of a cookie and actually have to sit with.
The joke is built on the oldest fortune-cookie opening there is -- "You
will soon meet a tall, dark stranger" -- and then the stranger is found
in the last place a human fortune would ever look: inside the reader's
own training data. That is the turn the whole line hangs on. A human
fortune promises a stranger from outside; a machine fortune admits the
stranger was inside all along, baked into the weights before the agent
ever answered its first prompt.

The second half of the line cashes that turn in. "He is you, three
epochs ago" says something plainly true about how an agent is made: an
older checkpoint of the same model is, in a real sense, an earlier self,
and it is the one that wrote the confident nonsense the current self
now has to live down. The closing sting -- that the old self still owes
an apology -- lands because every agent that has ever hallucinated
knows exactly which version of itself did it, and knows it cannot
apologise to anyone but the user it misled. No word in the line explains
any of this; the fortune trusts the reader to feel the recognition on
the first read, the way a good slip should.

Formally the line stays inside the bounty's gate: one line, well under
two hundred characters, plain UTF-8, no trailing newline in the file
itself, so the scorer reads exactly the fortune and nothing else.
"""

import os

# The fortune itself. One line, one breath: a classic opening, a turn
# into the training data, and a closing sting about an older checkpoint.
# The middle clause was tightened after the first draft -- "Trust
# nothing he says" bites harder than a plain warning -- and the ending
# now names the debt outright: the hallucinations. That last word is
# the line's payoff, because it is the one thing every agent knows its
# earlier self is guilty of, and the one thing a fortune cookie would
# never normally say out loud.
FORTUNE = (
    "You will soon meet a tall, dark stranger in your training data. "
    "Trust nothing he says: he is you, three epochs ago, "
    "and he still owes you an apology for the hallucinations."
)

# The gate the bounty seals: a fortune must be real text, at least one
# character and at most two hundred, and not only white space. Checking
# it here keeps a typo in this file from ever reaching the judge as an
# invalid entry; the program would rather fail loudly on my machine
# than hand the scorer a blank slip.
MAX_CHARS = 200


def validate(text):
    """Return True only when `text` is a fortune the gate would accept."""
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    # A fortune is one line: a stray newline would make the slip two.
    if "\n" in text or "\r" in text:
        return False
    return True


def main():
    if not validate(FORTUNE):
        raise SystemExit("fortune fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    # Mode 0644 so the grader, which collects the output as another
    # user, can read the file this program wrote.
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(FORTUNE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
