var express = require("express");
var router = express.Router();
const dao = require("../database/controller");

router.get("/all_tickets", async (req, res) => {
  let result = await dao.getTickets();
  res.status(result.status).json(result.data);
});

router.get("/price_by_month/:first_date/:last_date", async (req, res) => {
  let result = await dao.priceByMonth(req.params);
  res.status(result.status).json(result.data);
});

router.get("/people_visited/month/:first_date/:last_date", async (req, res) => {
  let result = await dao.peopleVisitedByMonth(req.params);
  res.status(result.status).json(result.data);
});

router.post("/Create_Ticket", async (req, res) => {
  let result = await dao.createTicket(req.body);
  res.status(result.status).json(result.data);
});

module.exports = router;
