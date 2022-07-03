const swaggerUi = require("swagger-ui-express");

require("dotenv").config();
const path = require("path");

const express = require("express");
const bodyParser = require("body-parser");
const app = express();
const port = process.env.SERVER_PORT;

const user_router = require("./routes/user");
const movie_router = require("./routes/movie");
const booking_router = require("./routes/booking");

const swaggerDocument = require("./apidocs/openapi.json");

var options = {
  customJs: "/custom.js",
};

app.use(
  "/api-docs",
  swaggerUi.serve,
  swaggerUi.setup(swaggerDocument, options)
);

app.use(bodyParser.json());

app.use(
  bodyParser.urlencoded({
    extended: true,
  })
);

app.get("/", (request, response) => {
  response.sendFile(path.join(__dirname, "./www/html/index.html"));
  //   response.json({ info: "Node.js, Express, and Postgres API" });
});

app.use("/api/v1", user_router);
app.use("/api/v1", movie_router);
app.use("/api/v1", booking_router);

app.listen(port, () => {
  console.log(`App running on port ${port}.`);
});
