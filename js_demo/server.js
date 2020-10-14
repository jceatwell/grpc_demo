const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader")
const packageDef = protoLoader.loadSync("proto/todo.proto", {});
const protoDescriptor = grpc.loadPackageDefinition(packageDef);
const todoPackage = protoDescriptor.todoPackage;

const SERVER_BINDING = "0.0.0.0:40000";

const server = new grpc.Server();
server.bind(SERVER_BINDING, grpc.ServerCredentials.createInsecure());
console.log(`Starting ${SERVER_BINDING}`);

server.addService(todoPackage.Todo.service, {
        "createTodo": createTodo,
        "readTodos" : readTodos,
        "readTodosStream": readTodosStream
    });
server.start();

const todos = []
function createTodo (call, callback) {
    console.log("createTodo() called ...")
    const todoItem = {
        "id": todos.length + 1,
        "details": call.request.details,
        "done": call.request.done? true : false
    }
    todos.push(todoItem)
    callback(null, todoItem); // callback(<length_of_payload>, <what_to_send>);
}

function readTodosStream(call, callback) {
    console.log("readTodosStream() called ...")
    todos.forEach(t => call.write(t));
    call.end();
}

function readTodos(call, callback) {
    console.log("readTodos() called ...")
    callback(null, {"items": todos})   
}