themeToggles = document.querySelectorAll("#theme-toggle");

const handleTheme = (theme) => {
    if (theme === "light") {
        bodyElement.classList.remove("dark");
        bodyElement.classList.add("light");
        localStorage.setItem("theme", "light");
        themeToggles.forEach((themeToggle) => {
            themeToggle.classList.remove("fa-sun");
            themeToggle.classList.add("fa-moon");
        });
    }

    if (theme === "dark") {
        bodyElement.classList.remove("light");
        bodyElement.classList.add("dark");
        localStorage.setItem("theme", "dark");

        themeToggles.forEach((themeToggle) => {
            themeToggle.classList.remove("fa-moon");
            themeToggle.classList.add("fa-sun");
        });
    }
};

document.addEventListener("DOMContentLoaded", () => {
    savedTheme = localStorage.getItem("theme");
    bodyElement = document.body;
    // themeToggle = document.querySelector("#theme-toggle");
    if (
        savedTheme === "dark" ||
        (!savedTheme &&
            window.matchMedia("(prefers-color-scheme: dark").matches)
    ) {
        bodyElement.classList.add("dark");
        handleTheme("dark");
    } else {
        bodyElement.classList.add("light");
        handleTheme("light");
    }

    themeToggles.forEach((themeToggle) => {
        themeToggle.addEventListener("click", () => {
            if (bodyElement.classList.contains("dark")) {
                handleTheme("light");
            } else {
                handleTheme("dark");
            }
        });
    });
});
