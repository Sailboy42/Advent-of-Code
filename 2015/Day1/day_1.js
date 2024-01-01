const fs = require('fs');
fs.readFile('Day1.txt', (err, data) => {
    if (err) throw err;
    let floorCommands = data.toString()
    //console.log(floorCommands)
    let floor = 0

let counter = 0
Array.from(floorCommands).forEach(elem => {
    counter++;
    floor += (elem === '(') - (elem === ')');

    if (floor === -1){
        console.log(counter);
    }
})

console.log(floor);

});