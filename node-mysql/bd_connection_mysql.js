const mysql = require('mysql');

const db = mysql.createConnection({
    host: 'labticvi2019.cevummruy0nm.us-east-2.rds.amazonaws.com',
    user: 'laboratorio',
    password: 'labtic2019',
    database: 'employees'
});

db.connect((err) => {
    if (err) {
        throw err;
    }
    console.log('Connected to database');
});

module.exports.getEmployees = (callback) => {
    db.query('SELECT * FROM employees LIMIT 10', (err, result) => {
        if (err) {
            throw err;
        }
        console.table(result);
        callback(result)
    });
};

