import { expect } from 'chai';
import { describe, it, before, afterEach, after } from 'mocha';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
    let queue;

    before(() => {
        // Initialize the queue in test mode
        queue = kue.createQueue();
        queue.testMode.enter();
    });

    afterEach(() => {
        // Clear the queue after each test
        queue.testMode.clear();
    });

    after(() => {
        // Exit test mode
        queue.testMode.exit();
    });

    it('should throw an error if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs('not an array', queue)).to.throw(
            'Jobs is not an array'
        );
    });

    it('should create jobs in the queue', () => {
        const jobs = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account',
            },
            {
                phoneNumber: '4153518781',
                message: 'This is the code 4562 to verify your account',
            },
        ];

        createPushNotificationsJobs(jobs, queue);

        // Verify the number of jobs in the queue
        expect(queue.testMode.jobs.length).to.equal(2);

        // Check that the jobs have the expected data
        expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
        expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);

        // Verify job type
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    });
});
