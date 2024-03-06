import { createQueue  } from "kue";

const queue = createQueue()

const jobData = {
    phoneNumber: '029200002',
    message: 'i am a message'
}

const job = queue.create('push_notification_code', jobData)
    .priority('high')
    .attempts(1)
    .save()

job
    .on('enqueue', () => {
        console.log(`Notification job created: ${job.id}`)
    })
    .on('complete', () => {
        console.log('Notification job completed')
    })
    .on('failed', () => {
        console.log('Notification job failed')
    })