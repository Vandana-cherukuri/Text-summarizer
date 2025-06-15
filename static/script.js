async function summarizeText() {
  const text = document.getElementById("inputText").value;

  const response = await fetch("/summarize", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ text: text })
  });

  const result = await response.json();

  if (result.summary) {
    document.getElementById("summaryOutput").innerText = result.summary;
  } else {
    document.getElementById("summaryOutput").innerText = "Error: " + result.error;
  }
}
