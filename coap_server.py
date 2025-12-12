import asyncio
from aiocoap import resource, Message, Context

class TimeResource(resource.Resource):
    async def render_get(self, request):
        return Message(payload=b"Hello! This is CoAP Server Time Resource")

async def main():
    # Create resource tree
    root = resource.Site()
    root.add_resource(['time'], TimeResource())

    # Start server
    await Context.create_server_context(root)
    print("CoAP Server is running on coap://localhost:5683/time")

    # Keep running forever
    await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())
