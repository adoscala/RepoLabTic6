const express = require('express');
const db = require('./bd_connection_mysql');

const app = express();

app.get('/employees', (req,res) => { 
    db.getEmployees((results) => {
        console.log(results)
        res.send(results)
    })
})

app.listen(3000, function () {
    console.log('Example app listening on port 3000!');
  });