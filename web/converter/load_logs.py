import os
import re
from typing import List, Tuple

from _io import TextIOWrapper

MATCH_DIGITS = re.compile(r'\:\s+(\d+)\s+', re.IGNORECASE)
MATCH_PLAYER = re.compile(r'NAME:\s+|\s+ID:\s+|\s+KILL:\s+', re.IGNORECASE)


Player = Tuple[str, str, int, int]


def process_team_line(line: str) -> str:

    return re.findall(MATCH_DIGITS, line)


def process_player_line(line: str) -> List[str]:

    _, name, id, kills = re.split(MATCH_PLAYER, line)

    kills = re.sub(r'\D', '', kills)

    return [name, int(id), int(kills)]


def process():

    with open(r'D:\rudie\py\converter\data\4.log') as f:
        process_single_log_file(f)


def process_single_log_file(*files: List[TextIOWrapper]) -> List[Player]:
    """
    Parse tournament results and return list of players sorted by
    Teams and kills
    """

    f = files[0]

    table = []

    team = 1

    for line in f.readlines():
        row = process_team_line(line)

        if len(row) != 4:
            row = [f"Команда {team}"] + process_player_line(line)
            table.append(row)
        else:
            team = int(process_team_line(line)[0])

    return sorted(table, key=lambda row: (int(row[0].split()[-1]), -row[-1]))


def process_multiple_files(*files: List[TextIOWrapper]) -> List[Player]:
    """
    Return list of players sorted by total kills
    """

    # {ID: [team, nickname, kills], ...}
    total = {}

    for file in files:

        results_list = process_single_log_file(file)

        # ID is the key of results dict
        results = {item[2]: item for item in results_list}

        for player_id, player in results.items():

            if player_id in total:
                total[player_id][-1] += player[-1]
            else:
                total[player_id] = player

    total_list = [[k, *v] for k, v in total.items()]

    return sorted(total_list, key=lambda player: -player[-1])
