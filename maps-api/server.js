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
  res.json({
    latitude: 19.0760,
    longitude: 72.8777,
    city: "Mumbai"
  });
});

app.listen(PORT, () => {
  console.log(`Maps API running on http://localhost:${PORT}`);
});