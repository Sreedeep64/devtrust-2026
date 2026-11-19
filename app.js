(() => {
  const data = window.DEVTRUST_DATA;
  const chart = document.querySelector("#chart");
  const chartTitle = document.querySelector("#chart-title");
  const chartSubtitle = document.querySelector("#chart-subtitle");
  const chartMeta = document.querySelector("#chart-meta");
  const sourceLink = document.querySelector("#chart-source");
  const tabs = [...document.querySelectorAll("[data-view]")];

  const formatValue = (item) => item.display || `${item.value.toFixed(1)}%`;

  function render(view) {
    const series = data[view];
    if (!series) return;

    chartTitle.textContent = series.title;
    chartSubtitle.textContent = series.subtitle;
    chartMeta.textContent = `${series.sample} · ${series.note}`;
    sourceLink.href = series.source;

    chart.replaceChildren();
    series.items.forEach((item, index) => {
      const row = document.createElement("div");
      row.className = "bar-row";
      row.style.setProperty("--delay", `${index * 55}ms`);

      const label = document.createElement("div");
      label.className = "bar-label";
      label.textContent = item.label;

      const track = document.createElement("div");
      track.className = "bar-track";
      track.setAttribute("role", "img");
      track.setAttribute("aria-label", `${item.label}: ${formatValue(item)}`);

      const fill = document.createElement("div");
      fill.className = `bar-fill is-${item.tone}`;
      fill.style.setProperty("--value", `${item.value}%`);

      const value = document.createElement("strong");
      value.className = "bar-value";
      value.textContent = formatValue(item);

      track.append(fill);
      row.append(label, track, value);
      chart.append(row);
    });

    tabs.forEach((tab) => {
      const isActive = tab.dataset.view === view;
      tab.classList.toggle("is-active", isActive);
      tab.setAttribute("aria-selected", String(isActive));
      tab.tabIndex = isActive ? 0 : -1;
    });
  }

  tabs.forEach((tab, index) => {
    tab.addEventListener("click", () => render(tab.dataset.view));
    tab.addEventListener("keydown", (event) => {
      if (!['ArrowLeft', 'ArrowRight'].includes(event.key)) return;
      event.preventDefault();
      const direction = event.key === 'ArrowRight' ? 1 : -1;
      const next = tabs[(index + direction + tabs.length) % tabs.length];
      next.focus();
      render(next.dataset.view);
    });
  });

  const risk = document.querySelector("#risk");
  const riskValue = document.querySelector("#risk-value");
  const policyTitle = document.querySelector("#policy-title");
  const policyCopy = document.querySelector("#policy-copy");
  const policyBadge = document.querySelector("#policy-badge");

  const policies = {
    1: ["Low risk", "Fast lane", "Use the tool, scan the result, and keep an easy undo path."],
    2: ["Routine", "Review", "Compare the output with nearby code or source material before accepting it."],
    3: ["Material", "Test", "Run locally and require relevant tests before the change moves forward."],
    4: ["High risk", "Second check", "Add security checks, source verification, and a named human reviewer."],
    5: ["Critical", "Human decision", "Use AI only for support. Keep the final judgment and approval with a person."]
  };

  function updatePolicy() {
    const [label, title, copy] = policies[risk.value];
    riskValue.textContent = label;
    policyTitle.textContent = title;
    policyCopy.textContent = copy;
    policyBadge.textContent = `Guardrail ${risk.value}/5`;
  }

  risk.addEventListener("input", updatePolicy);
  updatePolicy();
  render("trust");

  const year = document.querySelector("#year");
  year.textContent = new Date().getFullYear();
})();
