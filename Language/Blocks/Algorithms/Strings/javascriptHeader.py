header='''
process.stdin.resume();
process.stdin.setEncoding("utf-8");
var stdin_input = "";
let currentLine = 0;

process.stdin.on("data", function (input) {
    stdin_input += input;                   
});

process.stdin.on("end", function () {
   stdin_input = stdin_input.trim().split('\n');
   main();
});

function readLine() {
    return stdin_input[currentLine++];
}
'''