/**
 * Updates the current time display on the dashboard every second.
 */
function updateTime() {
    const now = new Date();
    // Format to local time string (e.g., "1:45:30 PM")
    const timeString = now.toLocaleTimeString();
    const timeElement = document.getElementById('current-time');
    if (timeElement) {
        timeElement.textContent = `Current Time: ${timeString}`;
    }
}

/**
 * Sets the 'Last Updated' timestamp on the dashboard.
 * @param {number} [ts] - A Unix timestamp (in seconds). If not provided,
 *                         the current client-side time is used as a fallback.
 */
function setLastUpdated(ts) {
    let timeString;
    if (ts) {
        // Convert Unix timestamp (seconds) to milliseconds for the Date object.
        const d = new Date(ts * 1000);
        // Format to a locale-specific date and time string.
        timeString = d.toLocaleString();
    } else {
        // Fallback to current time if no timestamp is provided.
        const now = new Date();
        timeString = now.toLocaleTimeString();
    }
    const updatedElement = document.getElementById('last-updated');
    if (updatedElement) {
        updatedElement.textContent = `Last Updated: ${timeString}`;
    }
}

/**
 * Fetches weather data from the backend API and updates the UI.
 * Handles loading states, errors, and successful data display.
 */
async function refreshWeather() {
    const btn = document.getElementById('refresh-weather');
    const weatherDataElement = document.getElementById('weather-data');

    try {
        // Disable the refresh button and show a loading state to prevent multiple clicks.
        if (btn) {
            btn.disabled = true;
            btn.classList.add('loading');
            btn.setAttribute('aria-busy', 'true');
        }

        // Fetch weather data from the '/weather' endpoint.
        // 'cache: no-store' ensures the latest data is always fetched.
        const res = await fetch('/weather', { cache: 'no-store' });

        // Handle non-successful HTTP responses.
        if (!res.ok) {
            throw new Error(`Server responded with status: ${res.status}`);
        }

        const data = await res.json();

        // Handle errors returned in the JSON payload from the backend.
        if (data.error) {
            throw new Error(data.error);
        }

        // On success, update the weather display with the formatted data.
        if (weatherDataElement) {
            weatherDataElement.innerHTML = `<pre>${data.formatted || 'No data available.'}</pre>`;
        }

        // Update the 'Last Updated' time using the reliable server timestamp.
        if (data.timestamp) {
            setLastUpdated(data.timestamp);
        }

    } catch (err) {
        // Display any caught errors in the weather data container for visibility.
        console.error('Error fetching weather:', err);
        if (weatherDataElement) {
            weatherDataElement.innerHTML = `<pre>Error: ${err.message}</pre>`;
        }
    } finally {
        // Re-enable the button and remove the loading state, regardless of outcome.
        if (btn) {
            btn.disabled = false;
            btn.classList.remove('loading');
            btn.removeAttribute('aria-busy');
        }
    }
}

// --- Event Listeners and Initializers ---

// This function runs when the page has finished loading.
window.addEventListener('load', () => {
    // Initialize the clock and set an interval to update it every second.
    updateTime();
    setInterval(updateTime, 1000);

    // Set an initial "loading" state for the last updated time.
    setLastUpdated();

    // Perform the initial weather data fetch as soon as the page loads.
    refreshWeather();

    // Set up an automatic refresh for the weather data every 5 minutes (300,000 ms).
    setInterval(refreshWeather, 5 * 60 * 1000);

    // Attach the refreshWeather function to the click event of the refresh button.
    const refreshButton = document.getElementById('refresh-weather');
    if (refreshButton) {
        refreshButton.addEventListener('click', refreshWeather);
    }
});
