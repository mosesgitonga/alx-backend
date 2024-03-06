import { createQueue  } from "kue";

//const myqueue = createQueue()

function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw Error('Jobs is not an array')
    }

    for (let job of jobs) {
        const newJob = queue.create('push_notification_code_3', job)
            .on('enqueue', () => {
                console.log(`Notification job created: ${newJob.id}`)
            })
            .on('complete', () => {
                console.log(`Notification job ${newJob.id} completed`)
            })
            .on('failed', (err) => {
                console.log(`Notification job ${newJob.id} failed: ${err}`)
            })
            .on('progress', () => {
                console.log(`Notification job ${newJob.id} ${newJob.progress()}% complete`)
            })
            .save()
    }
}

module.exports = createPushNotificationsJobs;