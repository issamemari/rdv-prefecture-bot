# Prefecture RDV Availability Checker Bot

This bot is designed to check for the availability of slots on the website of a French prefecture. Specifically, it checks for the availability of time slots ("guichet") and logs the results. The bot uses the `selenium` package to automate the web browser and interact with the website.

## Features:

- Allows users to specify the URL of the prefecture.
- Checks for availability periodically (with a default interval of 1 minute).
- Logs the availability status of each guichet.
- Runs in a Docker container with a headless Chrome browser.

## Prerequisites:

- Docker installed on your system.

## Setup:

1. **Clone the Repository:**
   ```bash
   git clone [repository-url]
   cd [repository-name]
   ```

2. **Build the Docker Image:**
   ```bash
   docker build -t guichet-bot .
   ```

## Usage:

1. **Run the bot:**
   ```bash
   docker run guichet-bot
   ```

   By default, the bot will check the availability every 1 minute at the URL `https://pprdv.interieur.gouv.fr`.

2. **Customize the bot's operation:**

   You can specify the prefecture URL and the period between checks using command-line arguments:

   ```bash
   docker run guichet-bot --prefecture-url [YOUR_URL] --period-minutes [PERIOD_IN_MINUTES]
   ```

   - `--prefecture-url`: Specifies the URL of the prefecture to check.
   - `--period-minutes`: Defines the interval (in minutes) between checks.

   For example:

   ```bash
   docker run guichet-bot --prefecture-url https://example.com --period-minutes 5
   ```

## Code Overview:

- **main.py**: Contains the primary logic for the bot, which automates the browser, navigates to the specified URL, checks the availability, and logs the results.

- **Dockerfile**: Describes the setup of the Docker container, including the installation of required packages and dependencies.

## Note:

Ensure your system has sufficient resources allocated for Docker as running browser automation tools might require more memory.

## Limitations:

This bot is specifically designed for the structure of the website `https://pprdv.interieur.gouv.fr`. Changes to the website's layout or flow might necessitate modifications to the bot's logic.

## Contributing:

Feel free to fork this repository, make changes, and create pull requests. Your contributions are welcome!

## License:

Please refer to the `LICENSE` file in the repository.

---

I hope this README helps you get started with the Guichet Availability Checker Bot! If you have any issues or questions, please open an issue in the repository.