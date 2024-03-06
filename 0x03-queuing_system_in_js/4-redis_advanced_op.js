import { createClient, print } from 'redis';

const client = createClient()

client
    .on('connect', () => {
        console.log('Redis client conncted to the server')
    })
    .on('error', (error) => {
        console.log(`Redis client not connected to the server: ${error}`)
    })
function createHash(hashKey, key, value) {
    client.hset(hashKey, key, value, print)
}


createHash('HolbertonSchools', 'portland', '50')
createHash('HolbertonSchools', 'seatle', '80')
createHash('HolbertonSchools', 'Newyork', '20')
createHash('HolbertonSchools', 'Bogota', '20')
createHash('HolbertonSchools', 'Cali', '40')
createHash('HolbertonSchools', 'paris', '2')

client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
        console.log('unable to get all objects', err)
    } else {
        console.log(reply)
    }
})