import os

import re

MATCH_DIGITS = re.compile('\D*(\d+)\D*', re.IGNORECASE)
MATCH_PLAYER = re.compile('NAME:\s+|\s+ID:\s+|\s+KILL:\s+', re.IGNORECASE)

def process_team_line(line: str) -> str:
    """
    TeamName:                      Rank: 1                    KillScore: 0                    RankScore: 0                    TotalScore: 0
    """
    return re.findall(MATCH_DIGITS, line)

def process_player_line(line: str) -> str:

    # return [re.sub('\s|\n', '', x) for x in re.findall(MATCH_PLAYER, line.strip())]
    # return re.findall(MATCH_PLAYER, line.strip())
    _, name, id, kill = re.split(MATCH_PLAYER, line)
    return [name, id, re.sub(r'\D', '', kill)]
    # return re.split(MATCH_PLAYER, line)


def process_log() -> None:

    table = list()

    with open(os.path.join('LOG Фаил клиента', '2.log'), 'r') as f:
        for i, line in enumerate(f.readlines()):

            row = process_team_line(line)

            if len(row) != 4:
                t = 2
                row = process_player_line(line)
            else:
                t = 1


            table.append({'type': t, 'content': row})
        return table
            # print(i, row)

            # print(f"****LINE {i}****".rjust(20, ' '))
            # print()
            # print(line)
            # print(row)
            # print()


            # line = re.sub('\s{2,}?', '', line.strip('\n\t'))
            # print(f"line {i}", line)
        # print(len(f.readlines()))


print(process_log())
