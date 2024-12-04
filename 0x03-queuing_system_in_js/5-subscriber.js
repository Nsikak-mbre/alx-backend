import { createClient } from "redis";

// create a new redis client
const client = createClient();

// connect to the redis server
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// log an error if the client is not connected to the server
client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error.message}`);
});

// subscribe to the channel 'holberton school channel'
client.subscribe('holberton school channel', (err) =>{
    if (err) {
        console.log(`Redis client not connected to the server: ${err}`);
    }
});

client.on('message', (channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
        client.unsubscribe(channel);
        client.quit();
    }
});