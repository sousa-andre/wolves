import asyncio

from wolves.factory.game.events import UserBanned
from wolves.game.game import ObservableGame

game = ObservableGame()
game.login('<your refresh token>')


async def main():
    req = await game.http.get_client_core('/playerRoleStats/totalWinCount')
    print(await req.json())

    await game.spectate()

    async for event in game.next_event():
        if isinstance(event, UserBanned):
            print("You're banned for", event.reason_message)
        else:
            print("Unknown event:", event)

    await game.cleanup()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

