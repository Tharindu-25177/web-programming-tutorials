import csv
from pathlib import Path

from players.models import Player, Position


POSITIONS = [
    ("Tight Head Prop", True),
    ("Hooker", True),
    ("Loose Head Prop", True),
    ("Second Row", False),
    ("Open Side Flanker", False),
    ("Blind Side Flanker", False),
    ("Number 8", False),
    ("Scrum Half", False),
    ("Fly Half", False),
    ("Inside Centre", False),
    ("Outside Centre", False),
    ("Left Wing", False),
    ("Right Wing", False),
    ("Full Back", False),
]


def run():
    # Create the rugby positions first.
    for position_name, is_specialist in POSITIONS:
        Position.objects.get_or_create(
            name=position_name,
            defaults={"specialist": is_specialist},
        )

    # Read player records from the CSV file.
    csv_file = Path(__file__).resolve().parent.parent / "data" / "players.csv"

    with csv_file.open("r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            player = Player.objects.create(
                first_name=row["first_name"],
                last_name=row["last_name"],
            )

            # Add the positions listed for this player.
            position_names = [
                name.strip()
                for name in row["positions"].split("|")
                if name.strip()
            ]

            for position_name in position_names:
                position = Position.objects.get(name=position_name)
                player.positions.add(position)

    print("Player data imported.")
