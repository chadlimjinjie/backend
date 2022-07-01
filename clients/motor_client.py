import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(
    'mongodb+srv://admin:admin@cluster0.tshns.mongodb.net/?retryWrites=true&w=majority'
)

db = client.myFirstDatabase
users_collection = db.users
