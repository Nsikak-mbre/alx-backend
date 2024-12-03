import { createClient } from "redis";

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

// connect the client 
client.connect();
