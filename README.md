# Prefecture RDV Availability Checker Bot

This bot is designed to check for the availability of slots on the website of a French prefecture. It monitors the availability of time slots in the different guichets and logs the results. When a slot becomes available, it sends an email notification. The bot uses the `selenium` package to automate the web browser and interact with the website.

## Features:

- Allows users to specify the URL of the prefecture.
- Sends an email notification when a guichet is available.
- Checks for availability periodically.
- Logs the availability status of each guichet.
- Runs in a Docker container with a headless Chrome browser.

## Prerequisites:

- Docker installed on your system.
- A Google email account (for SMTP).

## Setup:

1. **Clone the Repository:**
   ```bash
   git clone [repository-url]
   cd [repository-name]
   ```

2. **Setting up SMTP with Google:**
   
   Before the bot can send emails, you'll need to configure SMTP with Google:
   
   - Go to your [Google Account](https://myaccount.google.com/).
   - In the left navigation panel, click on `Security`.
   - Under “Signing in to Google,” select `App Passwords`. (You might need to sign in again).
   - Create a new app specific password, and name it appropriately, such as `RDV Prefecture Bot`
   - Note down the 16-character password. This will be your SMTP password.
   
   Do note that for this to work, you must have [2-Step Verification](https://www.google.com/landing/2step/) enabled on your Google account.

3. **Configure the bot using `config.json`:**
   
   Modify the `config.json` file in the root directory of the project to include your preferences and SMTP details:
   ```json
   {
       "prefecture_url": "YOUR_PREFECTURE_URL",
       "retry_period_seconds": YOUR_RETRY_PERIOD_IN_SECONDS,
       "to_email": "YOUR_NOTIFICATION_EMAIL_ADDRESS",
       "smtp": {
           "host": "smtp.gmail.com",
           "port": 587,
           "user": "YOUR_GOOGLE_EMAIL_ADDRESS",
           "password": "YOUR_GENERATED_APP_PASSWORD"
       }
   }
   ```

4. **Build the Docker Image:**
   ```bash
   docker build -t guichet-bot .
   ```

## Usage:

1. **Run the bot:**
   ```bash
   docker run guichet-bot
   ```

## Code Overview:

- **main.py**: Contains the primary logic for the bot. It automates the browser, navigates to the specified URL, checks availability, logs results, and sends email notifications.

- **Dockerfile**: Describes the setup of the Docker container, including the installation of required packages and dependencies.

## Note:

Ensure your system has sufficient resources allocated for Docker, as browser automation tools might require more memory.

## Limitations:

This bot is specifically tailored for the structure of the website `https://pprdv.interieur.gouv.fr`. Changes to the website's layout or flow might necessitate modifications to the bot's logic.

## Contributing:

Feel free to fork this repository, make changes, and create pull requests. Your contributions are appreciated!

## License:

Please refer to the `LICENSE` file in the repository.

---

I hope this README helps you get started with the Guichet Availability Checker Bot! If you have any issues or questions, please open an issue in the repository.