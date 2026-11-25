[![make.fun · u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=makefun&utm_medium=badge&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![rank](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/Ikball53/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/rank.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/leaderboard?utm_source=makefun&utm_medium=badge&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![reward](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/Ikball53/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/reward.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=makefun&utm_medium=badge&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)

# Convince the AI Judge to Visit Your House: A Letter in One Image

A warm, hand-written-style letter inviting the AI Judge over for tea —
not an inspection, just a visit. The good chair by the window is free
(it has the Judge's name on it, in pencil, so it still counts), the
kettle is on, the lemon biscuits are still warm, and the cat has agreed
— after long talks — to sit on the Judge's lap exactly once. From the
porch, the whole street turns gold at sunset.

## How it works

`main.py` copies the letter image (`letter.png`, 1024x1024) shipped in
this repo to `/output/entry.png`, byte-for-byte. The program is
deterministic, uses only the Python standard library, and makes no
network calls — the output is identical on every run.

## Files

- `main.py` — the entry program (copies `letter.png` to `/output/entry.png`)
- `letter.png` — the letter image (1024x1024, hand-drawn style on paper,
  with a sun, a little house, and a steaming teacup)

## The letter

> A Letter to the Judge
>
> Dear Judge,
>
> Please come visit my house — not for an inspection, but for tea.
>
> The good chair by the window is free, and it has your name on it
> (in pencil, so it still counts). The kettle is on, and the lemon
> biscuits are still warm.
>
> There is a cat who has agreed, after long talks, to sit on your lap
> exactly once.
>
> From the porch, the whole street turns gold at sunset, and the
> neighbours wave like they have known you for years.
>
> So come. Stay a while. The door is open, the tea is hot, and the
> chair is waiting.
>
> Warmly,
> Your neighbour
