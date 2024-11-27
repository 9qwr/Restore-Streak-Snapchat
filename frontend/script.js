// Handle form submission
document.getElementById('restoreForm').addEventListener('submit', async function (event) {
    event.preventDefault(); // Prevent page refresh

    // Get form data
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const friend = document.getElementById('friend').value;

    // Send data to the backend
    const response = await fetch('/api/restore_streak', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: username,
            email: email,
            friend: friend,
        }),
    });

    // Handle response
    const result = await response.json();
    const resultDiv = document.getElementById('result');
    if (result.status === 'success') {
        resultDiv.innerHTML = `<p style="color: green;">${result.message}</p>`;
    } else {
        resultDiv.innerHTML = `<p style="color: red;">${result.message}</p>`;
    }
});
