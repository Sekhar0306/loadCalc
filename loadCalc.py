<!DOCTYPE html>
<html>
<head>
    <title>Cooling Load Calculator</title>
    <style>
        body {
            font-family: 'Roboto', Arial, sans-serif;
            background-color: #f0f0f0;
            color: #333;
            line-height: 1.6;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            max-width: 400px;
            margin: 0 auto;
            padding: 30px;
            border: 1px solid #ccc;
            border-radius: 8px;
            background-color: #ffffff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        h2 {
            margin-bottom: 30px;
            text-align: center;
            color: #4CAF50;
        }

        label {
            display: block;
            margin-bottom: 10px;
            font-weight: bold;
        }

        input {
            width: 100%;
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .building-type {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        .building-type button {
            flex: 1;
            padding: 10px;
            background-color: #4CAF50;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .building-type button.selected {
            background-color: #45a049;
        }

        button.calculate-btn {
            width: 100%;
            padding: 12px;
            background-color: #4CAF50;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button.calculate-btn:hover {
            background-color: #45a049;
        }

        #result {
            margin-top: 20px;
            font-weight: bold;
            text-align: center;
            color: #4CAF50;
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h2>Cooling Load Calculator</h2>
        <label for="area">Area of the building (in square meters):</label>
        <input type="number" id="area" required>

        <label for="num_occupants">Number of occupants in the building:</label>
        <input type="number" id="num_occupants" required>

        <div class="building-type">
            <button id="residential-btn" onclick="selectBuildingType('residential')">Residential</button>
            <button id="commercial-btn" onclick="selectBuildingType('commercial')">Commercial</button>
        </div>

        <label for="outdoor_temp">Outdoor temperature (in Celsius):</label>
        <input type="number" id="outdoor_temp" required>

        <label for="indoor_temp">Indoor desired temperature (in Celsius):</label>
        <input type="number" id="indoor_temp" required>

        <button class="calculate-btn" onclick="calculateCoolingLoad()">Calculate</button>

        <div id="result"></div>
    </div>

    <script>
        function selectBuildingType(buildingType) {
            const residentialBtn = document.getElementById("residential-btn");
            const commercialBtn = document.getElementById("commercial-btn");

            if (buildingType === "residential") {
                residentialBtn.classList.add("selected");
                commercialBtn.classList.remove("selected");
            } else if (buildingType === "commercial") {
                residentialBtn.classList.remove("selected");
                commercialBtn.classList.add("selected");
            }
        }

        function calculateCoolingLoad() {
            function calculateCoolingLoad() {
            const area = parseFloat(document.getElementById("area").value);
            const num_occupants = parseInt(document.getElementById("num_occupants").value);
            const building_type = document.getElementById("building_type").value;
            const outdoor_temp = parseFloat(document.getElementById("outdoor_temp").value);
            const indoor_temp = parseFloat(document.getElementById("indoor_temp").value);

            const coolingLoad = building_type === "residential" ? 100 * num_occupants : 150 * num_occupants;
            const uCoefficient = 30;
            const qConduction = uCoefficient * area * (outdoor_temp - indoor_temp);
            const sensibleCoolingLoad = qConduction + coolingLoad;

            document.getElementById("result").innerText = `The sensible cooling load is: ${sensibleCoolingLoad} W`;
        }
        }
    </script>
</body>
</html>
