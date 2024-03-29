import { createClient, print } from 'redis';



const client = createClient();

client
  .on("connect", () => {
    console.log("Redis client connected to the server");
  })
  .on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  });

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print)
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, res) => {
        if (err) {
            console.error('unable to display value')
        } else {
            console.log(res)
        }
    })
}

displaySchoolValue('Holberton')
setNewSchool('Holbertonschool', '100')
displaySchoolValue('Holbertonschool')
