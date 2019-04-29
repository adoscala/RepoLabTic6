const knex = require('knex') ({
    client: 'mysql',
    connection: {
        host: 'labticvi2019.cevummruy0nm.us-east-2.rds.amazonaws.com',
        user: 'laboratorio',
        password: 'labtic2019',
        database: 'employees'
    }
});

knex.select().from('employees').then(function (result){
    console.log(result);
});

