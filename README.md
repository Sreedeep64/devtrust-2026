# DevTrust 2026

DevTrust is a compact, interactive data story about how developers use and verify AI tools. It turns selected findings from the 2026 Stack Overflow Developer Survey into one practical recommendation: design AI workflows for verification, not autopilot.

I chose this question because adoption numbers alone can hide the part that matters in real engineering work: what people do before they trust an answer enough to ship it. The result is a small, source-first case study rather than a general argument for or against AI.

**[Open the live case study](https://sreedeep64.github.io/devtrust-2026/)** · **[Download the one-slide findings PDF](https://sreedeep64.github.io/devtrust-2026/output/pdf/developer-ai-trust-2026.pdf)**

## What is included

- Three switchable views covering trust, validation habits, and workflow use
- A risk-based guardrail explorer that translates the finding into a design decision
- Clear sample sizes, question notes, primary sources, and limitations
- A responsive, accessible interface with no frameworks or external dependencies

## Run locally

Open `index.html` in a browser, or serve the folder from a local web server:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Data source

The full survey reports 30,903 valid responses across 169 countries. All figures used here are published aggregates from the [Stack Overflow Developer Survey 2026](https://survey.stackoverflow.co/2026/ai/data). The AI questions have smaller subsamples; their sample sizes vary and are shown in the interface.

## Important limitation

The Stack Overflow survey is voluntary. These findings describe its respondents and should not be treated as a census of every software developer or as evidence that one behavior causes another.
