import { createClient, print as redisPrint } from "redis"; 

// create a new Redis client
const client = createClient();

// connect to the Redis server
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// log an error if the client is not connected to the server
client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error.message}`);
});

function createHash() {
    client.hset('HolbertonSchools', 'Portland', '50', redisPrint);
    client.hset('HolbertonSchools', 'Seattle', '80', redisPrint);
    client.hset('HolbertonSchools', 'New York', '20', redisPrint);
    client.hset('HolbertonSchools', 'Bogota', '20', redisPrint);
    client.hset('HolbertonSchools', 'Cali', '40', redisPrint);
    client.hset('HolbertonSchools', 'Paris', '2', redisPrint);
}

// function to display the value for a given key
function displayHash() {
    client.hgetall('HolbertonSchools', (err, reply) => {
        if (err) {
            console.log(err);
        } else {
            console.log(reply);
        }
    });
}

// call the functions
createHash();
displayHash();
