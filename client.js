const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader")
const packageDef = protoLoader.loadSync("todo.proto", {});
const grpcObject = grpc.loadPackageDefinition(packageDef);
const todoPackage = grpcObject.todoPackage;

const text = process.argv[2];

const client = new todoPackage.Todo("localhost:40000", 
grpc.credentials.createInsecure())

client.createTodo({
    "id": -1,
    "text": text
}, (err, response) => {
    console.log("Received from server -> " + JSON.stringify(response, null, 2));
})

client.readTodos(null, (err, response) => {
    console.log("------- Full Response ------");
    console.log("Normal Send/Reveive: Items from Server: ");
    if (response.items)
        response.items.forEach((a,i) => console.log(`${i} -> ${a.text}`));
    console.log("------------------------------");
})

console.log("------- Stream Response ------");
const call = client.readTodosStream();
call.on("data", item => {
    console.log("received item from server " + JSON.stringify(item , null, 2))
})

call.on("end", e => console.log("server done!"))