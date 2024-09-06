from flask import Flask, jsonify
from flask_cors import CORS
import fastf1
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/race-data/<int:year>/<string:race>/<string:session>')
def get_race_data(year, race, session):
    fastf1.Cache.enable_cache('cache')  # Enable caching
    race_session = fastf1.get_session(year, race, session)
    race_session.load()

    drivers = []
    for driver in race_session.drivers:
        laps = race_session.laps.pick_driver(driver)
        lap_times = laps['LapTime'].dt.total_seconds().tolist()
        lap_times = [None if np.isnan(time) else time for time in lap_times]
        drivers.append({
            'name': race_session.get_driver(driver)['FullName'],
            'lapTimes': lap_times
        })

    race_data = {
        'race': f"{race} Grand Prix",
        'laps': len(race_session.laps),
        'drivers': drivers
    }

    return jsonify(race_data)

if __name__ == '__main__':
    app.run(debug=True)