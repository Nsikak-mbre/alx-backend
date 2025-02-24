import { createClient, print as redisPrint } from 'redis';

// Create a new Redis client
const client = createClient();

// Connect to the Redis server
client.on('connect', () => {
    console.log('Redis client connected to the server')
});

// Log an error if the client is not connected to the server
client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error.message}`)
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redisPrint)
}

// logs the value for the key passed to it
function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        if (err) {
            console.log(err);
        } else {
            console.log(reply);
        }
    })
}

// call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
