const API_URL = "http://127.0.0.1:8000";

const codeInput = document.getElementById("code-input");
const charCount = document.getElementById("char-count");
const reviewBtn = document.getElementById("review-btn");
const btnText = document.getElementById("btn-text");
const btnSpinner = document.getElementById("btn-spinner");
const summaryBar = document.getElementById("summary-bar");

codeInput.addEventListener("input", () => {
  const len = codeInput.value.length;
  charCount.textContent = `${len} / 10000 characters`;
  if (len > 9000) {
    charCount.style.color = "#f85149";
  } else {
    charCount.style.color = "#8b949e";
  }
});

async function reviewCode() {
  const code = codeInput.value.trim();

  if (!code) {
    shakeButton();
    return;
  }

  setLoading(true);
  clearResults();

  try {
    const response = await fetch(`${API_URL}/review`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code })
    });

    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`);
    }

    const data = await response.json();
    displayResults(data);

  } catch (error) {
    displayError(error.message);
  } finally {
    setLoading(false);
  }
}

function displayResults(data) {
  const categories = ["bugs", "security", "quality", "suggestions"];

  categories.forEach(category => {
    const list = document.getElementById(`list-${category}`);
    const count = document.getElementById(`count-${category}`);
    const summaryCount = document.getElementById(`s-${category}`);
    const items = data[category] || [];

    list.innerHTML = "";
    count.textContent = items.length;
    summaryCount.textContent = items.length;

    if (items.length === 0) {
      const li = document.createElement("li");
      li.className = "none-found";
      li.textContent = "None found — looks good.";
      list.appendChild(li);
    } else {
      items.forEach(item => {
        const li = document.createElement("li");
        li.textContent = item;
        list.appendChild(li);
      });
    }
  });

  summaryBar.classList.remove("hidden");
  summaryBar.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

function displayError(message) {
  const list = document.getElementById("list-bugs");
  list.innerHTML = "";
  const li = document.createElement("li");
  li.style.color = "#f85149";
  li.textContent = `Error: ${message}. Make sure the backend is running.`;
  list.appendChild(li);
}

function clearResults() {
  const categories = ["bugs", "security", "quality", "suggestions"];
  categories.forEach(category => {
    const list = document.getElementById(`list-${category}`);
    const count = document.getElementById(`count-${category}`);
    list.innerHTML = `<li class="empty-item">Submit code to see results</li>`;
    count.textContent = "0";
  });
  summaryBar.classList.add("hidden");
}

function setLoading(state) {
  reviewBtn.disabled = state;
  btnText.textContent = state ? "Analysing..." : "Review My Code";
  btnSpinner.classList.toggle("hidden", !state);
}

function shakeButton() {
  reviewBtn.style.transform = "translateX(-6px)";
  setTimeout(() => reviewBtn.style.transform = "translateX(6px)", 100);
  setTimeout(() => reviewBtn.style.transform = "translateX(-4px)", 200);
  setTimeout(() => reviewBtn.style.transform = "translateX(0)", 300);
}

document.addEventListener("keydown", (e) => {
  if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
    reviewCode();
  }
});