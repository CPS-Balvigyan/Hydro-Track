from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iot_device_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class DeviceData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(50), nullable=False)
    device_type = db.Column(db.String(50), nullable=False)
    sensor_1 = db.Column(db.Float, nullable=False)
    sensor_2 = db.Column(db.Float, nullable=False)
    sensor_3 = db.Column(db.Float, nullable=False)
    sensor_4 = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "device_id": self.device_id,
            "device_type": self.device_type,
            "sensor_1": self.sensor_1,
            "sensor_2": self.sensor_2,
            "sensor_3": self.sensor_3,
            "sensor_4": self.sensor_4,
            "timestamp": self.timestamp.isoformat()
        }

# Initialize Database
with app.app_context():
    db.create_all()

# API to add device data
@app.route('/api/add_device_data', methods=['POST'])
def add_device_data():
    data = request.json

    try:
        new_data = DeviceData(
            device_id=data['device_id'],
            device_type=data['device_type'],
            sensor_1=data['sensor_1'],
            sensor_2=data['sensor_2'],
            sensor_3=data['sensor_3'],
            sensor_4=data['sensor_4']
        )
        db.session.add(new_data)
        db.session.commit()
        return jsonify({"message": "Device data added successfully"}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field in JSON: {e}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API to fetch all device data
@app.route('/api/get_device_data', methods=['GET'])
def get_device_data():
    try:
        data = DeviceData.query.all()
        return jsonify([item.to_dict() for item in data]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
