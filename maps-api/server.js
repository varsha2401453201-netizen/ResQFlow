const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

const PORT = 5001;

app.get("/", (req, res) => {
  res.json({
    message: "ResQFlow Maps API is running"
  });
});

app.get("/api/location", (req, res) => {
  const { latitude, longitude } = req.query;

  if (!latitude || !longitude) {
    return res.status(400).json({
      error: "Latitude and longitude are required"
    });
  }

  res.json({
    latitude: Number(latitude),
    longitude: Number(longitude)
  });
});

app.listen(PORT, () => {
  console.log(`Maps API running on http://localhost:${PORT}`);
});