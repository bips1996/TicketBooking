var express = require("express");
var router = express.Router();
const dao = require("../database/controller");

router.get("/all_movies", async (req, res) => {
  let result = await dao.getMovies();
  res.status(result.status).json(result.data);
});

router.post("/Create_Movie", async (req, res) => {
  let result = await dao.createMovieRecord(req.body);
  res.status(result.status).json(result.data);
});

module.exports = router;
