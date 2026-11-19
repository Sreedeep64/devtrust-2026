window.DEVTRUST_DATA = {
  trust: {
    title: "Trust depends on verifiability",
    subtitle: "How respondents described their trust in AI output at work",
    sample: "n = 14,304",
    note: "Single-choice question",
    source: "https://survey.stackoverflow.co/2026/ai/data#trust-in-ai-tools",
    items: [
      { label: "When I can easily verify it", value: 48.0, tone: "primary" },
      { label: "For many tasks, not important decisions", value: 16.3, tone: "secondary" },
      { label: "For low-risk tasks only", value: 16.3, tone: "secondary" },
      { label: "Do not trust it for most work tasks", value: 12.3, tone: "warning" },
      { label: "Including important work decisions", value: 6.6, tone: "accent" }
    ]
  },
  validation: {
    title: "Most developers check before they ship",
    subtitle: "Actions taken before using an AI-generated answer",
    sample: "n = 13,162",
    note: "Multiple selections allowed",
    source: "https://survey.stackoverflow.co/2026/ai/data#next-steps-after-receiving-an-ai-prompt-response",
    items: [
      { label: "Run it locally", value: 76.5, tone: "primary" },
      { label: "Compare against codebase context", value: 63.9, tone: "secondary" },
      { label: "Inspect tests or security implications", value: 53.0, tone: "secondary" },
      { label: "Read official documentation", value: 38.0, tone: "accent" },
      { label: "Use it as-is", value: 9.6, tone: "warning" }
    ]
  },
  workflow: {
    title: "Adoption follows the cost of a mistake",
    subtitle: "Share currently using AI or AI agents for selected workflow tasks",
    sample: "Survey question with task-level response bases",
    note: "Selected categories from the full table",
    source: "https://survey.stackoverflow.co/2026/ai/data#ai-workflow-current-and-expected",
    items: [
      { label: "Generating code in familiar areas", value: 68.9, display: "69%", tone: "primary" },
      { label: "Debugging, troubleshooting or refactoring", value: 63.8, tone: "secondary" },
      { label: "Writing or improving tests", value: 58.1, tone: "secondary" },
      { label: "Writing communications", value: 23.5, tone: "accent" },
      { label: "Production operations or troubleshooting", value: 19.9, tone: "warning" }
    ]
  }
};
