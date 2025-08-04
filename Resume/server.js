// counter.js
window.onload = function () {
  fetch("http://127.0.0.1:5000/views")
    .then(response => response.json())
    .then(data => {
      document.getElementById("view-count").innerText = data.views;
    })
    .catch(error => {
      console.error("Fetch failed:", error);
      document.getElementById("view-count").innerText = "N/A";
    });
};
