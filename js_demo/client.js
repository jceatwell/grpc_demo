const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader")
const packageDef = protoLoader.loadSync("proto/todo.proto", {});
const protoDescriptor = grpc.loadPackageDefinition(packageDef);
const todoPackage = protoDescriptor.todoPackage;

const details = process.argv[2];

// Create Insecure Connection (NOte that this can use OAuth / SSL)
const stub = new todoPackage.Todo("localhost:40000", grpc.credentials.createInsecure())

// Stub - Standard client (POST)
stub.createTodo({
    "id": -1,
    "details": details,
    "done": false
}, (err, response) => {
    console.log("Received from server (NEW) -> " + JSON.stringify(response, null, 2));
})

// Stub (GET)
stub.readTodos(null, (err, response) => {
    console.log("------- Full Response ------");
    console.log("Normal Send/Reveive: Items from Server: ");
    if (response.items)
        response.items.forEach((a,i) => console.log(`${i} -> ${a.details} is ${a.done}`));
    console.log("------------------------------");
})

// Stub (Streaming from Server)
console.log("------- Stream Response ------");
const call = stub.readTodosStream();
call.on("data", item => {
    console.log("received item from server " + JSON.stringify(item , null, 2))
})

call.on("end", e => console.log("server done!"))