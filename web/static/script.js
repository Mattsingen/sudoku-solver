document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('sudoku-form');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        const puzzle = formData.get('puzzle');

        fetch('/solve', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ puzzle: puzzle }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                resultDiv.innerHTML = `<h3>Solved Puzzle:</h3><pre>${data.solution}</pre>`;
            } else {
                resultDiv.innerHTML = `<h3>Error:</h3><p>${data.message}</p>`;
            }
        })
        .catch(error => {
            resultDiv.innerHTML = `<h3>Error:</h3><p>${error.message}</p>`;
        });
    });
});