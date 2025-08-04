 <script>
    document.addEventListener("DOMContentLoaded", () => {
      fetch("https://crc-fa0m.onrender.com/views")
        .then((response) => response.json())
        .then((data) => {
          document.getElementById("view-count").innerText = data.views;
        })
        .catch((error) => {
          console.error("Error fetching view count:", error);
          document.getElementById("view-count").innerText = "N/A";
        });
    });
  </script>
