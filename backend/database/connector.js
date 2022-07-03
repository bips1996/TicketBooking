require("dotenv").config();
const Client = require("pg").Client;
const client = new Client({
  user: process.env.DB_USERNAME,
  host: process.env.DB_HOST,
  database: process.env.DB_NAME,
  password: process.env.DB_PASSWORD,
  port: process.env.DB_HOST_SERVER_PORT,
});
client.connect();
module.exports = {
  client,
};
