const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader")
const packageDef = protoLoader.loadSync("proto/todo.proto", {});
const protoDescriptor = grpc.loadPackageDefinition(packageDef);
const todoPackage = protoDescriptor.todoPackage;

const cmd = process.argv[2];
const task = process.argv[3];

// Create Insecure Connection (NOte that this can use OAuth / SSL)
const stub = new todoPackage.Todo("localhost:40000", grpc.credentials.createInsecure())

function createToDo(details) {
    stub.createTodo({
        "id": -1,
        "details": details,
        "done": false
    }, (err, response) => {
        console.log("Received from server (NEW) -> " + JSON.stringify(response, null, 2));
    })
}

function getToDo() {
    stub.readTodos(null, (err, response) => {
        console.log("------- Full Response ------");
        console.log("Normal Send/Reveive: Items from Server: ");
        if (response.items)
            response.items.forEach((a,i) => console.log(`${i} -> ${a.details} is ${a.done}`));
        console.log("------------------------------");
    })
}

function streanResponse() {
    console.log("------- Stream Response ------");
    const call = stub.readTodosStream();
    call.on("data", item => {
        console.log("received item from server " + JSON.stringify(item , null, 2))
    })

    call.on("end", e => console.log("server done!"))
}

switch(cmd) {
    case "add": 
        createToDo(task);
        break;
    case "get":
        getToDo();
        break;
    case "stream":
        streanResponse();
        break;
}
