document.getElementById("spinButton").addEventListener("click", function () {
    const spinner = document.getElementById("spinner");
    spinner.classList.add("spinning");

    // Fetch result from the backend
    fetch('/spin')
        .then(response => response.json())
        .then(data => {
            setTimeout(() => {
                spinner.classList.remove("spinning");
                document.getElementById("movie").textContent = `Movie: ${data.movie}`;
                document.getElementById("meal").textContent = `Meal: ${data.meal}`;
            }, 2000); // Simulate spin duration
        });
});