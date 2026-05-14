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
    

    address1 = fake.street_address()

    city = fake.city()

    state_province = fake.state()

    country = fake.country()

    postal_code = fake.postcode()

    birthdate = fake.date_of_birth(
        minimum_age=21,
        maximum_age=80
    )

    gender = random.choice([
        "Male",
        "Female"
    ])

    home_phone = fake.phone_number()

    mobile_phone = fake.phone_number()

    alt_phone = fake.phone_number()

    email_domains = [
        "gmail.com",
        "yahoo.com",
        "outlook.com",
        "hotmail.com"
    ]

    email = (
        first_name.lower() +
        "." +
        last_name.lower() +
        "@" +
        random.choice(email_domains)
    )


    ##################################
    # Dynamic Host / CMP Data
    ##################################
    # Reset random seed for dynamic values
    random.seed(None)
    fake.seed_instance(None)


    entity_action = random.choice([
        "GAME:TABLE_PLAY",
        "GAME:SLOT_PLAY"
    ])
    current_host = fake.name()

    host_email_domains = [
        "casinohost.com",
        "vipservices.com",
        "grandroyale.com"
    ]

    properties = {
        "GRC": "Grand Royale Casino",
        "AC": "Atlantis Casino",
        "RRC": "Red Rock Casino"
    }

    current_host_email = (
        
        current_host.lower().replace(" ", ".") +
        str(random.randint(1, 999)) +
        "@" +
        random.choice(host_email_domains)
    )

    

    current_host_sf_property_id = random.choice(
        list(properties.keys())
    )

    current_host_property_name = properties[
        current_host_sf_property_id
    ]

    cmp_preferred_property_id = random.choice(
        list(properties.keys())
    )

    cmp_preferred_property_distance_miles = round(
        random.uniform(1, 100),
        2
    )

    cmp_closest_property_distance_miles = round(
        random.uniform(1, 50),
        2
    )

    cmp_closest_property_id = random.choice(
        list(properties.keys())
    )

    cmp_closest_property_name = properties[
        cmp_closest_property_id
    ]

    player_territory = random.choice([
        "East",
        "West",
        "North",
        "South"
    ])

    player_marketarea = random.choice([
        "Vegas",
        "California",
        "Texas",
        "Florida"
    ])

    cmp_mail_optedin = random.choice([
        True,
        False
    ])

    cmp_sms_optedin = random.choice([
        True,
        False
    ])

    cmp_email_optedin = random.choice([
        True,
        False
    ])

    ##################################
    # Default Boolean Flags
    ##################################

    is_active = True

    is_active_player = True

    is_banned = False

    is_banned_player = False

    is_no_mail = False

    is_return_mail = False

 

    
    

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

    casino_name = properties[
        current_host_sf_property_id
    ]

    timestamp = datetime.now() - timedelta(
        days=days_back,
        seconds=seconds_back
    )

    current_host_start_date = (
    timestamp - timedelta(days=10)
    ).date()

    current_host_stop_date = (
        timestamp + timedelta(days=90)
    ).date()

    ############################
    game_tran_id = fake.uuid4()

    game_club_level = club_level

    game_cash_buy_in = round(
        random.uniform(10, 500),
        2
    )

    game_credit_buy_in = round(
        random.uniform(0, 300),
        2
    )

    game_chip_buy_in = round(
        random.uniform(0, 1000),
        2
    )

    game_promo_buy_in = round(
        random.uniform(0, 200),
        2
    )

    game_plays = random.randint(1, 500)

    game_unadjusted_theo = round(
        theo_win + random.uniform(1, 50),
        2
    )

    game_net_theo_win = round(
        theo_win - random.uniform(0, 20),
        2
    )

    game_net_casino_win = round(
        casino_win - random.uniform(0, 50),
        2
    )

    game_cmp_game_name = game_title

    game_cmp_game_id = random.randint(
        1000,
        9999
    )

    game_jackpot_amount = round(
        random.uniform(0, 50000),
        2
    )

    player_value = round(
        random.uniform(1.0, 30.0),
        4
    )

    #####
    if entity_action == "GAME:SLOT_PLAY":

        has_played_slot_game = "Y"
    else:

        has_played_slot_game = "N"

    if has_played_slot_game == "Y":

        has_played_table_game = "N"

        # Slot data
        game_machine_mfr = random.choice([
            "IGT",
            "Aristocrat",
            "Konami"
        ])

        game_machine_model = random.choice([
            "A560",
            "Raptor",
            "A600"
        ])

        game_machine_location = (
            f"Zone-{random.randint(1,10)}"
        )

        game_machine_section = (
            f"Section-{random.randint(1,20)}"
        )

        game_machine_bank = (
            f"Bank-{random.randint(1,50)}"
        )

        game_machine_position = random.randint(
            1,
            10
        )

        game_machine_is_leased = random.choice([
            True,
            False
        ])

        game_machine_lease_rate_type = (
            random.choice([
                "Fixed",
                "Revenue Share"
            ])
        )

        game_machine_cabinet_type = (
            random.choice([
                "Slant",
                "Curve"
            ])
        )

        game_machine_sds_game_title = (
            game_title
        )

        game_machine_sas_serial_number = (
            serial_number
        )

        game_machine_pls_game_theme = (
            random.choice([
                "Asian",
                "Classic",
                "Vegas"
            ])
        )

        # Table columns EMPTY
        game_table_average_bet = None
        game_table_walked_with = None
        game_table_game_type = None
        game_table_location = None
        game_table_pit_no = None
        game_table_table_no = None
        game_table_seat_no = None
        game_table_freq_id = None
        game_table_is_void = None

    else:

        has_played_table_game = "Y"

        # Table game data
        game_table_average_bet = round(
            random.uniform(5, 500),
            2
        )

        game_table_walked_with = round(
            random.uniform(-5000, 10000),
            2
        )

        game_table_game_type = random.choice([
            "Blackjack",
            "Roulette",
            "Baccarat",
            "Poker"
        ])

        game_table_location = (
            f"Pit-{random.randint(1,10)}"
        )

        game_table_pit_no = random.randint(
            1,
            20
        )

        game_table_table_no = random.randint(
            1,
            200
        )

        game_table_seat_no = random.randint(
            1,
            8
        )

        game_table_freq_id = random.choice([
            "DAILY",
            "WEEKLY",
            "MONTHLY"
        ])

        game_table_is_void = random.choice([
            True,
            False
        ])

        # Slot columns EMPTY
        game_machine_mfr = None
        game_machine_model = None
        game_machine_location = None
        game_machine_section = None
        game_machine_bank = None
        game_machine_position = None
        game_machine_is_leased = None
        game_machine_lease_rate_type = None
        game_machine_cabinet_type = None
        game_machine_sds_game_title = None
        game_machine_sas_serial_number = None
        game_machine_pls_game_theme = None


    return {

        "PERSONID": personid,

        "ACTIVECLUBID": activeclubid,

        "PERSON_FIRST_NAME": first_name,

        "PERSON_LAST_NAME": last_name,

        "ADDRESS1": address1,

        "CITY": city,

        "STATE_PROVINCE": state_province,

        "COUNTRY": country,

        "POSTAL_CODE": postal_code,

        "BIRTHDATE": birthdate.isoformat(),

        "GENDER": gender,

        "HOME_PHONE": home_phone,

        "MOBILE_PHONE": mobile_phone,

        "ALT_PHONE": alt_phone,

        "EMAIL": email,

        "IS_ACTIVE": is_active,

        "IS_ACTIVE_PLAYER": is_active_player,

        "IS_BANNED": is_banned,

        "IS_BANNED_PLAYER": is_banned_player,

        "IS_NO_MAIL": is_no_mail,

        "IS_RETURN_MAIL": is_return_mail,

        "CURRENT_HOST": current_host,

        "CURRENT_HOST_EMAIL": current_host_email,

        "CURRENT_HOST_START_DATE":
            current_host_start_date.isoformat(),

        "CURRENT_HOST_STOP_DATE":
            current_host_stop_date.isoformat(),

        "CURRENT_HOST_SF_PROPERTY_ID":
            current_host_sf_property_id,

        "CURRENT_HOST_PROPERTY_NAME":
            current_host_property_name,

        "CMP_PREFERRED_PROPERTY_ID":
            cmp_preferred_property_id,

        "CMP_PREFERRED_PROPERTY_DISTANCE_MILES":
            cmp_preferred_property_distance_miles,

        "CMP_CLOSEST_PROPERTY_DISTANCE_MILES":
            cmp_closest_property_distance_miles,

        "CMP_CLOSEST_PROPERTY_ID":
            cmp_closest_property_id,

        "CMP_CLOSEST_PROPERTY_NAME":
            cmp_closest_property_name,

        "PLAYER_TERRITORY":
            player_territory,

        "PLAYER_MARKETAREA":
            player_marketarea,

        "CMP_MAIL_OPTEDIN":
            cmp_mail_optedin,

        "CMP_SMS_OPTEDIN":
            cmp_sms_optedin,

        "CMP_EMAIL_OPTEDIN":
            cmp_email_optedin,

        "ENTITY_ACTION": entity_action,

        "EVENT_ID": fake.bothify(text='EV-########'),

        "EVENT_TIMESTAMP": timestamp.isoformat(),

        "GAMING_DATE": timestamp.strftime("%Y-%m-%d"),

        "CLUB_LEVEL": club_level,

        "TIER_POINTS": random.randint(10, 500),

        

        "TRANSACTION_AMOUNT": bet,

        "PLAYER_VALUE": player_value,

        "GAME_THEO_WIN": theo_win,

        "GAME_CASINO_WIN": casino_win,

        "GAME_GROSS_WIN": casino_win,

        "GAME_TRAN_ID": game_tran_id,


        "GAME_GAME_TITLE": game_title,

        "GAME_CASINO_NAME": casino_name,

        "GAME_CLUB_LEVEL": game_club_level,

        "GAME_CASH_BUY_IN": game_cash_buy_in,

        "GAME_CREDIT_BUY_IN": game_credit_buy_in,

        "GAME_CHIP_BUY_IN": game_chip_buy_in,

        "GAME_PROMO_BUY_IN": game_promo_buy_in,

        "GAME_PLAYS": game_plays,

        "GAME_BET": bet,

        "GAME_PAID_OUT": paid_out,

        
        "GAME_UNADJUSTED_THEO":
            game_unadjusted_theo,

        "GAME_HOLD_PCT": round(
            hold_pct * 100,
            2
        ),

        "GAME_LOCATION": f"Zone-{random.randint(1, 10)}",

        "HAS_PLAYED_SLOT_GAME": has_played_slot_game,

        "HAS_PLAYED_TABLE_GAME":
            has_played_table_game,

        "GAME_NET_THEO_WIN":
            game_net_theo_win,

        "GAME_NET_CASINO_WIN":
            game_net_casino_win,

        "GAME_CMP_GAME_NAME":
            game_cmp_game_name,

        "GAME_CMP_GAME_ID":
            game_cmp_game_id,

        "GAME_MACHINE_MFR":
            game_machine_mfr,

        "GAME_MACHINE_MODEL":
            game_machine_model,
        
        "GAME_MACHINE_SERIAL_NUMBER": serial_number,

        "GAME_MACHINE_GAME_TYPE": random.choice([
            "Slot",
            "Video Poker",
            "Electronic Table"
        ]),

        

        
        

        
        

        "GAME_MACHINE_LOCATION":
            game_machine_location,

        "GAME_MACHINE_SECTION":
            game_machine_section,

        "GAME_MACHINE_BANK":
            game_machine_bank,

        "GAME_MACHINE_POSITION":
            game_machine_position,

        "GAME_MACHINE_IS_LEASED":
            game_machine_is_leased,

        "GAME_MACHINE_LEASE_RATE_TYPE":
            game_machine_lease_rate_type,

        "GAME_MACHINE_CABINET_TYPE":
            game_machine_cabinet_type,

        "GAME_JACKPOT_AMOUNT":
            game_jackpot_amount,

        "GAME_MACHINE_SDS_GAME_TITLE":
            game_machine_sds_game_title,

        "GAME_MACHINE_SAS_SERIAL_NUMBER":
            game_machine_sas_serial_number,

        

        "GAME_TABLE_AVERAGE_BET":
            game_table_average_bet,

        "GAME_TABLE_WALKED_WITH":
            game_table_walked_with,

        "GAME_TABLE_GAME_TYPE":
            game_table_game_type,

        "GAME_TABLE_LOCATION":
            game_table_location,

        "GAME_TABLE_PIT_NO":
            game_table_pit_no,

        "GAME_TABLE_TABLE_NO":
            game_table_table_no,

        "GAME_TABLE_SEAT_NO":
            game_table_seat_no,

        "GAME_TABLE_FREQ_ID":
            game_table_freq_id,

        "GAME_TABLE_IS_VOID":
            game_table_is_void,

        "LOAD_TIMESTAMP": datetime.now().isoformat()
    }


@app.get("/v1/player-activity")
async def get_player_activity(
    players: int = 500,
    records_per_player: int = 3
):
    """
    Returns players with multiple gaming records.
    Each player keeps same identity details
    but has many gameplay transactions.
    """

    records = []

    used_names = set()

    i = 0

    while len(used_names) < players:

        # Stable UUID
        fake.seed_instance(i)

        player_id = fake.uuid4()

        sample_record = generate_gaming_record(
            person_id=player_id
        )

        full_name = (
            sample_record["PERSON_FIRST_NAME"] +
            " " +
            sample_record["PERSON_LAST_NAME"]
        )

        # Ensure unique player names
        if full_name not in used_names:

            used_names.add(full_name)

            # Generate multiple records
            for _ in range(records_per_player):

                records.append(
                    generate_gaming_record(
                        person_id=player_id
                    )
                )

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
