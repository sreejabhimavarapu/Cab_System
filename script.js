document.getElementById('bookingForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let source = document.getElementById('source').value;
    let destination = document.getElementById('destination').value;

    // Send API request to backend (Python) with source and destination
    fetch(`/api/book_cab?source=${source}&destination=${destination}`)
        .then(response => response.json())
        .then(data => {
            let resultElement = document.getElementById('result');
            resultElement.innerHTML = `<p>Shortest time: ${data.shortestTime} minutes</p>
                                       <p>Estimated cost: $${data.estimatedCost}</p>`;
        })
        .catch(error => console.error('Error:', error));
});
