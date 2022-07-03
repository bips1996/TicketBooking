const client = require("./connector").client;

//user daos
const getUsers = async () => {
  let result = await client
    .query("SELECT * FROM user_details ORDER BY id ASC")
    .then(function (results) {
      return {
        status: 200,
        data: results.rows,
      };
    })
    .catch(function (err) {
      console.log("error = ", err);
      throw err;
    });
  return result;
};

const createUser = async (params) => {
  let result = await client
    .query("INSERT INTO user_details(email,name) VALUES($1,$2) returning *", [
      params.email,
      params.name,
    ])
    .then(function (results) {
      return {
        status: 201,
        data: results.rows[0],
      };
    })
    .catch(function (err) {
      console.log("error = ", err);
      if (err.detail) {
        return {
          status: 409,
          data: err.detail,
        };
      }
      throw err;
    });
  return result;
};

//movie daos
const getMovies = async () => {
  let result = await client
    .query("SELECT * FROM movie_details ORDER BY id ASC")
    .then(function (results) {
      return {
        status: 200,
        data: results.rows,
      };
    })
    .catch(function (err) {
      console.log("error = ", err);
      throw err;
    });
  return result;
};

const createMovieRecord = async (params) => {
  let result = await client
    .query(
      "INSERT INTO movie_details(title,release_date) VALUES($1,$2) returning *",
      [params.title, params.release_date]
    )
    .then(function (results) {
      return {
        status: 201,
        data: results.rows[0],
      };
    })
    .catch(function (err) {
      console.log("error = ", err);
      if (err.detail) {
        return {
          status: 409,
          data: err.detail,
        };
      }
      throw err;
    });
  return result;
};

//booking daos

const getTickets = async () => {
  let result = await client
    .query("SELECT * FROM tickets ORDER BY id ASC")
    .then(function (results) {
      return {
        status: 200,
        data: results.rows,
      };
    })
    .catch(function (err) {
      console.log("error = ", err);
      throw err;
    });
  return result;
};

const priceByMonth = async (params) => {
  let result = await client
    .query(
      "SELECT TO_CHAR(created_date, 'month') AS month, \
      SUM(no_of_tickets*ticket_price::numeric) AS summary_profit FROM public.tickets \
      WHERE created_date BETWEEN Date($1) \
      AND Date($2) \
      GROUP BY month \
      ORDER BY EXTRACT(MONTH FROM TO_DATE(TO_CHAR(created_date, 'month'), 'Month')) asc;",
      [params.first_date, params.last_date]
    )
    .then(function (results) {
      return {
        status: 200,
        data: results.rows,
      };
    })
    .catch(function (err) {
      console.log("error = ", err);
      throw err;
    });
  return result;
};

const peopleVisitedByMonth = async (params) => {
  let result = await client
    .query(
      "SELECT TO_CHAR(created_date, 'month') AS month, SUM(no_of_tickets) AS summary_visits \
      FROM public.tickets \
      WHERE created_date \
      BETWEEN Date($1) AND Date($2) \
      GROUP BY month \
      ORDER BY EXTRACT(MONTH FROM TO_DATE(TO_CHAR(created_date, 'month'), 'Month')) asc;",
      [params.first_date, params.last_date]
    )
    .then(function (results) {
      return {
        status: 200,
        data: results.rows,
      };
    })
    .catch(function (err) {
      console.log("error = ", err);
      throw err;
    });
  return result;
};

const createTicket = async (params) => {
  let result = await client
    .query(
      "INSERT INTO tickets(customer,movie,created_date,movie_time,ticket_price,no_of_tickets) \
      VALUES($1,$2,$3,$4,$5,$6) returning *",
      [
        params.customer,
        params.movie,
        params.created_date,
        params.movie_time,
        params.ticket_price,
        params.no_of_tickets,
      ]
    )
    .then(function (results) {
      return {
        status: 201,
        data: results.rows[0],
      };
    })
    .catch(function (err) {
      console.log("error = ", err);
      if (err.detail) {
        return {
          status: 409,
          data: err.detail,
        };
      }
      throw err;
    });
  return result;
};

module.exports = {
  getUsers,
  createUser,
  createMovieRecord,
  getMovies,
  getTickets,
  createTicket,
  priceByMonth,
  peopleVisitedByMonth,
};
