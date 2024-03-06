import kue from 'kue';
import createPushNotificationsJobs from './8-job.js'; 
import { expect } from 'chai';

describe('createPushNotificationsJobs function', () => {
  let queue;

  before(() => {
    queue = kue.createQueue();
  });

  beforeEach(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
   
    queue.testMode.clear();
  });

  after(() => {
  
    queue.testMode.exit();
  });

  it('should create jobs in the queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(jobs.length);

    queue.testMode.jobs.forEach(job => {
      expect(job.type).to.equal('push_notification_code_3');
    });


  });
});