import { createClient, print } from 'redis';
import { promisify } from 'util'


const client = createClient();

client
  .on("connect", () => {
    console.log("Redis client connected to the server");
  })
  .on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  });

const getAsync = promisify(client.get).bind(client)

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print)
}

async function displaySchoolValue(schoolName) {
        try  {
            const res = await getAsync(schoolName);
            console.log(res);
            
        } catch {
            console.error('unable to display value')
        }
   
}

displaySchoolValue('Holberton')
setNewSchool('Holbertonschool', '100')
displaySchoolValue('Holbertonschool')