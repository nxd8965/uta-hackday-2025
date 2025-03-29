/* script.js */
document.addEventListener('DOMContentLoaded', function() {
    const predictButton = document.getElementById('predict_button');
    const predictionDiv = document.getElementById('prediction');
    const errorDiv = document.getElementById('error');

    predictButton.addEventListener('click', function() {
        // Clear previous messages
        predictionDiv.textContent = '';
        errorDiv.textContent = '';

        // Get selected row index
        const selectedRow = document.querySelector('input[name="selected_row"]:checked');

        if (!selectedRow) {
            errorDiv.textContent = 'Please select a row.';
            return;
        }

        const rowIndex = selectedRow.value;

        // Make AJAX request
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `row_index=${rowIndex}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                errorDiv.textContent = `Error: ${data.error}`;
            } else {
                predictionDiv.textContent = `Prediction: ${data.prediction}`;
            }
        })
        .catch(error => {
            console.error('Fetch error:', error);
            errorDiv.textContent = 'An error occurred while making the request.';
        });
    });
});