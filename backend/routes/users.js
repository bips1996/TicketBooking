var express = require("express");
var router = express.Router();

/* GET users listing. */
/**
 * @swagger
 * /customers:
 *  get:
 *    description: Use to request all customers
 *    responses:
 *      '200':
 *        description: A successful response
 */
router.get("/user", function (req, res, next) {
  res.send("respond with a resource");
});

module.exports = router;
