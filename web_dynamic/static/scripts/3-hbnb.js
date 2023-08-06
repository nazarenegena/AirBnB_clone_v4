document.addEventListener('DOMContentLoaded', function () {
    const url = 'http://0.0.0.0:5001/api/v1/places_search/';

    function createArticle(place) {
        const article = document.createElement('article');
        article.innerHTML = `
            <div class="title_box">
                <h2>${place.name}</h2>
                <div class="price_by_night">$${place.price_by_night}</div>
            </div>
            <div class="information">
                <div class="max_guest">${place.max_guest} Guest${place.max_guest !== 1 ? 's' : ''}</div>
                <div class="number_rooms">${place.number_rooms} Bedroom${place.number_rooms !== 1 ? 's' : ''}</div>
                <div class="number_bathrooms">${place.number_bathrooms} Bathroom${place.number_bathrooms !== 1 ? 's' : ''}</div>
            </div>
            <div class="user">
                <!-- Remove the Owner tag here -->
            </div>
            <div class="description">
                ${place.description}
            </div>
        `;
        return article;
    }

    fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({})
    })
    .then(response => response.json())
    .then(data => {
        const placesSection = document.querySelector('.places');
        data.forEach(place => {
            placesSection.appendChild(createArticle(place));
        });
    });
});

