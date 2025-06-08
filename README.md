# Birdeye API Scripts

This project contains a collection of Python scripts that interact with the Birdeye.so API to fetch various cryptocurrency-related data. Each script is designed to be run independently and demonstrates a specific API endpoint.

## Table of Contents
- [Project Overview](#project-overview)
- [File Explanations](#file-explanations)
  - [`main.py`](#mainpy)
  - [`pnl.py`](#pnlpy)
  - [`top_profiles.py`](#topprofilespy)
  - [`post.py`](#postpy)
- [Setup and How to Run](#setup-and-how-to-run)
- [Important Notes](#important-notes)

## Project Overview

The scripts in this repository showcase how to retrieve data from Birdeye's multi-chain API. The examples include fetching trader information, profit and loss leaderboards, top profiles (whales and airdrop recipients), and sending POST requests for transaction data.

## File Explanations

### `main.py`

This script performs a simple GET request to a hardcoded Birdeye API endpoint to fetch trader data for a specific token on the Solana blockchain.

**Flowchart:**

```mermaid
graph TD;
    A["Start"] --> B["Define API URL and Headers"];
    B --> C["Make GET request to Birdeye API for trader token data"];
    C --> D["Print response text"];
    D --> E["End"];
```

### `pnl.py`

This script fetches the top 7-day gainers from the Birdeye PnL leaderboard. It parses the JSON response and prints the profit and wallet address for each trader in the list.

**Flowchart:**

```mermaid
graph TD;
    A["Start"] --> B["Define API URL and Headers for PnL leaderboard"];
    B --> C["Make GET request to Birdeye API"];
    C --> D{"Response OK?"};
    D -- Yes --> E["Parse JSON response"];
    E --> F["Extract 'items' from data"];
    F --> G["Loop through each item"];
    G --> H["Extract 7-day PnL and address"];
    H --> I["Print profit and address"];
    I --> G;
    G -- Loop finished --> J["End"];
    D -- No --> K["Print error (not implemented)"];
    K --> J;
```

### `top_profiles.py`

This script retrieves information about top profiles on Birdeye, specifically focusing on "Top Airdrop" recipients and "Top Whales". It then prints the wallet address and today's trading volume for each profile in both categories.

**Flowchart:**

```mermaid
graph TD;
    A["Start"] --> B["Define API URL and Headers for top profiles"];
    B --> C["Make GET request to Birdeye API"];
    C --> D{"Response OK?"};
    D -- Yes --> E["Parse JSON response"];
    E --> F["Extract 'data'"];
    F --> G["Loop through 'topAirdrop' list"];
    G --> H["Extract wallet and today's volume"];
    H --> I["Print Airdrop wallet and volume"];
    I --> G;
    G -- Loop finished --> J["Loop through 'topWhale' list"];
    J --> K["Extract wallet and today's volume"];
    K --> L["Print Whale wallet and volume"];
    L --> J;
    J -- Loop finished --> M["End"];
    D -- No --> N["Print error (not implemented)"];
    N --> M;
```

### `post.py`

This script demonstrates how to send POST requests to the Birdeye API. It contains a function that repeatedly sends a request for token transaction data and prints the HTTP status code of the response. The script is set to make 10 requests.

**Flowchart:**

```mermaid
graph TD;
    A["Start"] --> B["Define 'post_request' function"];
    B --> C["Call 'post_request(10)'"];
    subgraph post_request
        D["Start function"] --> E["Define Headers and JSON data"];
        E --> F["Start loop (for specified repetitions)"];
        F --> G["Make POST request to Birdeye API"];
        G --> H["Print response status code"];
        H --> F;
        F -- Loop finished --> I["End function"];
    end
    C --> I;
    I --> J["End Program"];
```

## Setup and How to Run

### Prerequisites

- Python 3.x
- `pip` for package installation

### Installation

The scripts use the `curl_cffi` library to make HTTP requests, as it can impersonate browser TLS fingerprints. Install it using pip:

```bash
pip install curl_cffi
```

### Running the Scripts

Each script can be run directly from the terminal.

```bash
# To run the main script
python main.py

# To run the PnL script
python pnl.py

# To run the top profiles script
python top_profiles.py

# To run the post request script
python post.py
```

## Important Notes

- **Hardcoded Values**: All scripts contain hardcoded API URLs and headers. These might need to be updated if the Birdeye API changes.
- **Expired JWT in `post.py`**: The `post.py` script contains a hardcoded `cf-be` JWT in the headers. This token is likely expired and will need to be replaced with a valid one for the request to succeed. You would typically obtain this by observing the network requests in your browser when using the Birdeye website. 