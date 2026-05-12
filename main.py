from fastapi import FastAPI
from faker import Faker
import random
import hashlib
from datetime import datetime
from datetime import datetime, timedelta
import uvicorn

app = FastAPI(title="Casino Gaming Data API")

fake = Faker()


def generate_gaming_record(person_id: str):
    """
    Generates persistent player profile data
    with dynamic gaming transaction data.
    """

    # Stable hash from person_id
    stable_hash = int(
        hashlib.md5(person_id.encode()).hexdigest(),
        16
    ) % (10**8)

    # Seed faker/random for stable profile
    fake.seed_instance(stable_hash)
    random.seed(stable_hash)

    # Persistent player info
    first_name = fake.first_name()
    last_name = fake.last_name()

    club_level = random.choice(
        ["Gold", "Silver", "Platinum", "Diamond"]
    )

    serial_number = fake.bothify(
        text='SN-####-####'
    )

    game_title = random.choice([
        "88 Fortunes",
        "Buffalo Gold",
        "Wheel of Fortune",
        "Blackjack T1"
    ])

    # Stable PERSONID
    personid = fake.numerify(
        text='######'
    )

    # Stable ACTIVECLUBID (13 digits)
    activeclubid = fake.numerify(
        text='#############'
    )

    # Stable ENTITY_ACTION
    entity_action = random.choice([
        "GAME:TABLE_PLAY",
        "GAME:SLOT_PLAY"
    ])

    # Reset random seed for dynamic values
    random.seed(None)

    # Dynamic gaming transaction values
    bet = round(
        random.uniform(1.0, 100.0),
        2
    )

    hold_pct = random.uniform(0.05, 0.15)

    theo_win = round(
        bet * hold_pct,
        2
    )

    win_chance = random.random()

    if win_chance > 0.6:
        paid_out = round(
            bet * random.uniform(1.2, 5.0),
            2
        )
    else:
        paid_out = 0.0

    casino_win = round(
        bet - paid_out,
        2
    )

        # Random timestamp within last 1 year
    days_back = random.randint(0, 365)

    seconds_back = random.randint(
        0,
        86400
    )

    casino_name = random.choice([
    "Grand Royale Casino",
    "Bellagio Resort",
    "Caesars Palace",
    "MGM Grand",
    "Wynn Las Vegas",
    "Venetian Casino",
    "Marina Bay Sands",
    "Resorts World",
    "Hard Rock Casino",
    "Golden Nugget",
    "Atlantis Casino",
    "Red Rock Casino",
    "Sunset Station",
    "Cosmopolitan Casino",
    "Treasure Island Casino"
    ])

    timestamp = datetime.now() - timedelta(
        days=days_back,
        seconds=seconds_back
    )

    return {
        "UNIVERSAL_PERSON_KEY": person_id,

        "PERSONID": personid,

        "ACTIVECLUBID": activeclubid,

        "PERSON_FIRST_NAME": first_name,

        "PERSON_LAST_NAME": last_name,

        "ENTITY_ACTION": entity_action,

        "EVENT_ID": fake.bothify(text='EV-########'),

        "EVENT_TIMESTAMP": timestamp.isoformat(),

        "GAMING_DATE": timestamp.strftime("%Y-%m-%d"),

        "CLUB_LEVEL": club_level,

        "TIER_POINTS": random.randint(10, 500),

        "TRANSACTION_AMOUNT": bet,

        "GAME_THEO_WIN": theo_win,

        "GAME_CASINO_WIN": casino_win,

        "GAME_GROSS_WIN": casino_win,

        "GAME_GAME_TITLE": game_title,

        "GAME_CASINO_NAME": casino_name,

        "GAME_BET": bet,

        "GAME_PAID_OUT": paid_out,

        "GAME_HOLD_PCT": round(
            hold_pct * 100,
            2
        ),

        "GAME_LOCATION": f"Zone-{random.randint(1, 10)}",

        "GAME_MACHINE_SERIAL_NUMBER": serial_number,

        "GAME_MACHINE_GAME_TYPE": random.choice([
            "Slot",
            "Video Poker",
            "Electronic Table"
        ]),

        "HAS_PLAYED_SLOT_GAME": "Y",

        "LOAD_TIMESTAMP": datetime.now().isoformat()
    }


@app.get("/v1/player-activity")
async def get_player_activity(limit: int = 5000):
    """
    Returns 5000 stable players
    with unique names and dynamic gameplay.
    """

    records = []

    used_names = set()

    i = 0

    while len(records) < limit:

        # Stable faker-generated UUID
        fake.seed_instance(i)

        player_id = fake.uuid4()

        record = generate_gaming_record(
            person_id=player_id
        )

        full_name = (
            record["PERSON_FIRST_NAME"] +
            " " +
            record["PERSON_LAST_NAME"]
        )

        # Ensure unique names
        if full_name not in used_names:

            used_names.add(full_name)

            records.append(record)

        i += 1

    return records


@app.get("/v1/player/{person_id}")
async def get_specific_player(person_id: str):
    """
    Returns a specific persistent player
    with dynamic gaming activity.
    """

    return generate_gaming_record(
        person_id=person_id
    )


if __name__ == "__main__":

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )
