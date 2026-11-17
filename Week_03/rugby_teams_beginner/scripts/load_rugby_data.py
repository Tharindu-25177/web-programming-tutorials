import csv
from pathlib import Path
from teams.models import Player, Position


POSITIONS = [
    ('Tight Head Prop', True),
    ('Hooker', True),
    ('Loose Head Prop', True),
    ('Second Row', False),
    ('Open Side Flanker', False),
    ('Blind Side Flanker', False),
    ('Number 8', False),
    ('Scrum Half', False),
    ('Fly Half', False),
    ('Inside Centre', False),
    ('Outside Centre', False),
    ('Left Wing', False),
    ('Right Wing', False),
    ('Full Back', False),
]


def run():
    # Add the positions first so that players can be linked to them.
    for position_name, is_specialist in POSITIONS:
        Position.objects.get_or_create(
            name=position_name,
            defaults={'is_specialist': is_specialist}
        )

    if Player.objects.exists():
        print('Player data already exists. No CSV rows were loaded.')
        return

    csv_path = Path('players.csv')
    if not csv_path.exists():
        print('players.csv was not found. Put it in the main project folder.')
        return

    with csv_path.open(newline='', encoding='utf-8-sig') as csv_file:
        for row in csv.DictReader(csv_file):
            player = Player.objects.create(
                first_name=row['first_name'],
                last_name=row['last_name'],
                age=int(row['age']),
                email=row.get('email', ''),
                specialist_eligible=row['specialist_eligible'].strip().lower() == 'yes'
            )

            # Positions in the CSV must be separated with a | symbol.
            position_names = row['positions'].split('|')
            for position_name in position_names:
                position_name = position_name.strip()
                if position_name:
                    position = Position.objects.get(name=position_name)
                    if position.is_specialist and not player.specialist_eligible:
                        print('Skipped specialist position for', player)
                    else:
                        player.positions.add(position)

            print('Loaded:', player)
