
// COMMON JAVASCRIPT FILE


// Logout confirmation
function logoutConfirm() {
    if (confirm("Are you sure you want to logout?")) {
        window.location.href = "login.html";
    }
}

// Simple welcome message
window.onload = function () {
    console.log("Student Performance Prediction System Loaded");
};

// Utility function (percentage calculator)
function calculatePercentage(marksArray) {
    let total = 0;
    marksArray.forEach(mark => total += mark);
    return (total / marksArray.length).toFixed(2);
}