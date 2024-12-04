import kue from 'kue';

// Blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notifications
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100); // Start progress tracking
  console.log(`Notification job #${job.id} 0% complete`);

  // Check if phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    console.log(`Notification job #${job.id} failed: Phone number ${phoneNumber} is blacklisted`);
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  setTimeout(() => {
    job.progress(50, 100); // Midway progress tracking
    console.log(`Notification job #${job.id} 50% complete`);

    // Simulate notification sending
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    job.progress(100, 100); // Complete progress tracking
    console.log(`Notification job #${job.id} completed`);
    done(); // Mark job as done
  }, 500); // Simulate processing delay
}

// Create a queue
const queue = kue.createQueue();

// Process jobs in the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
