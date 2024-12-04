import kue from 'kue';

// Create a queue
const queue = kue.createQueue();

// define a job
const jobData = {
    phoneNumber: '08072552341',
    message: 'This is the code to verify your account'
};

// create a new job with the jobData
const job = queue.create('push_notification_code', jobData)
    .save((err) => {
        if (!err){
            console.log(`Notification job created: ${job.id}`);
        } else {
            console.error(`Failed to create a job: ${err.message}`);
        }
    });

    // Event listener for jon completion
    job.on('complete', () => {
        console.log('Notification job completed');
    });

    job.on('failed', () => {
        console.error(`Notification job failed`);
    });

