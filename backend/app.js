const express = require("express");
const app = express();
app.use(express.json());
app.use(require("cors")());

app.get("/api/pois", (req, res) => {
  res.json([{ id: 1, name: "栈桥", lng: 120.32, lat: 36.06 }]);
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
