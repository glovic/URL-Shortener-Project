async function shortenURL() {
    const urlInput = document.getElementById('url-input').value;
    if (urlInput) {
        const response = await fetch('http://localhost:5000/api/shorten', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                original_url: urlInput
            })
        });
        const result = await response.json();
        window.location.href = 'copy_page.html?short_url=' + encodeURIComponent(result.short_url);
    }
}