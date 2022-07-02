require("dotenv").config();
const Client = require("pg").Client;
const client = new Client({
  user: process.env.DB_USERNAME,
  host: "localhost",
  database: "ticketbook",
  password: "Bips@1234",
  port: 5432,
});
client.connect();
module.exports = {
  client,
};
