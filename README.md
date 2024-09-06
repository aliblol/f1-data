# F1 Data API

This project provides an API to fetch Formula 1 race data using the `fastf1` library. The API allows users to retrieve race data, including lap times for drivers, for specific races and sessions.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/aliblol/f1-data-api.git
    cd f1-data-api
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. The API will be available at `http://127.0.0.1:5000`.

## Endpoints

### Get Race Data

- **URL**: `/api/race-data/<int:year>/<string:race>/<string:session>`
- **Method**: `GET`
- **URL Parameters**:
  - `year`: The year of the race (e.g., `2021`).
  - `race`: The name of the race (e.g., `Bahrain`).
  - `session`: The session type (e.g., `Race`, `Qualifying`).

- **Response**:
  ```json
  {
    "race": "Bahrain Grand Prix",
    "laps": 57,
    "drivers": [
      {
        "name": "Lewis Hamilton",
        "lapTimes": [90.123, 89.456, null, ...]
      },
      ...
    ]
  }