import { createClient, print as redisPrint } from 'redis';
import { promisify } from 'util';

// Create a new Redis client
const client = createClient();

// Connect to the Redis server
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Log an error if the client is not connected to the server
client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error.message}`);
});

// Promisify the `get` method
const getAsync = promisify(client.get).bind(client);

// Function to set a new value in Redis
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redisPrint);
}

// Function to display the value for a given key using async/await
async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (error) {
        console.error(error);
    }
}

// Call the functions
(async () => {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();
