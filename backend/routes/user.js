var express = require("express");
var router = express.Router();
const dao = require("../database/controller");

router.get("/all_users", async (req, res) => {
  let result = await dao.getUsers();
  res.status(result.status).json(result.data);
});

router.post("/Create_User", async (req, res) => {
  let result = await dao.createUser(req.body);
  res.status(result.status).json(result.data);
});

module.exports = router;
