// making it so $ gets HTML values
const $ = function (selector) {
    return document.querySelector(selector);
};

let countriesData = []; // making the array that will store all the country data
let chartInstance = null; // making the chart variable so it can be updated or destroyed 

// update table function 
const updateCountryTable = (data) => {
    console.log(data); // log data so i can verify im getting it

    // make headers for table
    let tableContent = `<tr class="w3-teal">
        <th>Flag</th>
        <th>Country Name</th>
        <th>Capital</th>
        <th>Region</th>
        <th>Language</th>
        <th>Currency</th>
        <th>Population</th>
        <th>Latitude</th>
        <th>Longitude</th>
    </tr>`;

    // go through each countries data and set it so i can put it into the table
    data.forEach((country) => {
        const name = country.name.common; // the country name
        const cap = country.capital; // the capital
        const region = country.region; // the region
        const language = country.languages ? Object.values(country.languages).join(", ") : "Unknown";
        // languages and a check for null to get rid of an error i was getting 
        const money = country.currencies ? Object.values(country.currencies).map(c => c.name).join(", ") : "Unknown";
        // currencies and a check for null to get rid of an error i was getting
        const pop = country.population; // the population
        const lat = country.latlng; // the latitude
        const long = country.latlng; // the longitude
        const flagUrl = country.flags.png; // the countries flag

        // make a row with all the current countries data
        tableContent += `<tr>
            <td><img src="${flagUrl}" alt="Flag of ${name}" class="w3-image" style="max-width: 40px;" /></td>
            <td>${name}</td>
            <td>${cap}</td>
            <td>${region}</td>
            <td>${language}</td>
            <td>${money}</td>
            <td>${pop}</td>
            <td>${lat}</td>
            <td>${long}</td>
        </tr>`;
    });

    // update the html table so it shows up
    $("#countriesTable").innerHTML = tableContent;
};

// the function to fetch and display weather data
const fetchWeatherData = (latitude, longitude) => {
    const weatherUrl = `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m&daily=weather_code,temperature_2m_max,temperature_2m_min&timezone=auto`;

    fetch(weatherUrl)
        .then((response) => response.json()) // parsing the JSON response
        .then((data) => {
            console.log(data); // log data so i can verify im getting it
            const labels = data.daily.time; // get the dates
            const maxTemps = data.daily.temperature_2m_max; // get the maximum temperatures
            const minTemps = data.daily.temperature_2m_min; // get the minimum temperatures
            updateWeatherChart(labels, maxTemps, minTemps); // update the chart with the new data
        })
        .catch((error) => console.error("Error fetching weather data:", error)); // handle any errors
};

// update the weather chart function
const updateWeatherChart = (labels, maxTemps, minTemps) => {
    // destroy the existing chart if it exists
    if (chartInstance) {
        chartInstance.destroy();
    }

    // making a new chart with data from the country
    chartInstance = new Chart("myChart", {
        type: "line",
        data: {
            labels: labels, // my x-axis label, which is the dates
            datasets: [
                {
                    label: "Max Temperature (°C)",
                    fill: false,
                    borderColor: "rgba(255, 0, 0, 0.5)", // a red line for the max temps
                    backgroundColor: "rgba(255, 0, 0, 1)",
                    data: maxTemps, // the points for the max temps
                },
                {
                    label: "Min Temperature (°C)",
                    fill: false,
                    borderColor: "rgba(0, 0, 255, 0.5)", // a blue line for the min temps
                    backgroundColor: "rgba(0, 0, 255, 1)",
                    data: minTemps, // the points for the min temps
                },
            ],
        },
        options: {
            legend: { display: true }, // the display "min max" at the top of the chart
            scales: {
                yAxes: [
                    {
                        ticks: {
                            min: Math.min(...minTemps), // minimum temperature for the y-axis
                            max: Math.max(...maxTemps), // maximum temperature for the y-axis
                        },
                    },
                ],
            },
        },
    });
};

// the event listener for the search bar
$("#searchBar").addEventListener("input", (event) => {
    const searchTerm = event.target.value; // search
    const filteredCountries = countriesData.filter((country) =>
        country.name.common.toLowerCase().includes(searchTerm)
    ); // only get the countries that have whatevers in the search term

    updateCountryTable(filteredCountries); // update the table again with the new results

    // if only one of the countries matches show me weather data from there
    if (filteredCountries.length === 1) {
        const { latlng } = filteredCountries[0];
        fetchWeatherData(latlng[0], latlng[1]);
    } else {
        // destroy the chart if no country matches or if theres more than 1
        if (chartInstance) {
            chartInstance.destroy();
        }
    }
});

// fetch the country data when the page loads
document.addEventListener("DOMContentLoaded", () => {
    fetch("https://restcountries.com/v3.1/all?fields=name,capital,region,languages,currencies,population,latlng,flags") // fetch the data from the API
        .then((response) => response.json()) // parsing the JSON response
        .then((data) => {
            countriesData = data; // store the data globally for use in filtering and displaying
            updateCountryTable(countriesData); // Display all countries initially
        })
        .catch((error) => console.error("Error fetching country data:", error)); // handle any errors
});
