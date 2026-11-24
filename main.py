"""One Word From Grandma — make.fun entry.

Writes exactly one word to /output/entry.txt: the single word a grandma
would text about AI. The judge compares words pairwise on, in order:
(1) it reads as the one word she would text about AI, (2) real grandma
texting voice — warm, a little baffled, (3) funny in one word with no
context, (4) tied to AI/machines, (5) fresh, not the obvious pick, and
instantly readable. Fixed house texts play in every heat and a
byte-identical entry can never win, so the obvious picks are traps.

Head-to-head against the judge's ordered criteria:
- "robot": the obvious pick — dies on (5) and is a plausible house text.
- "ChatGTP" (pass 1): the transposed-letter typo she would really make.
  Strongest on (4), but the joke takes a beat to spot, a typo is an
  error rather than her voice, and it is a well-worn internet joke the
  field will crowd into — a plausible strong house text.
- "unplug": her universal fix for any machine, but it is an instruction,
  not her reaction in her own voice, and it is not warm.
- "haunted": vivid and baffled, but it fits any creaky house — the AI
  tie on (4) is weaker.
- "smartypants" (final): the word she calls anyone who answers every
  question instantly, in full sentences, with total confidence — the AI
  to a tee. It wins on (2), the first criterion where the rivals
  differ: it is her actual texting voice, warm with a wobble of
  bafflement that the thing talks back. It lands in one read on (3),
  it is tied to AI through its defining trait on (4) — it knows
  everything and tells you so — and on (5) it is a fresh pick the
  field is not crowded into, still instantly readable.
"""

WORD = "smartypants"


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(WORD)


if __name__ == "__main__":
    main()
