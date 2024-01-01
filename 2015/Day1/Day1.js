
// Requiring fs module in which 
// readFile function is defined.
const fs = require('fs');
 
fs.readFile('Day1.txt', (err, floor_commands) => {
  if (err) throw err;
 
  console.log(commands.toString());
});
