#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, async (err, res, body) => {
  err && console.log(err);

  const charArray = JSON.parse(res.body).characters;
  for (const char of charArray) {
    await new Promise((resolve, reject) => {
      request(char, (err, res, body) => {
        err && console.log(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
