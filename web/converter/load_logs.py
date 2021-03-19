import re
from typing import List, Tuple, Dict
from pprint import pprint


from _io import TextIOWrapper

MATCH_DIGITS = re.compile(r'\:\s+(\d+)\s+', re.IGNORECASE)
MATCH_TEAM = re.compile(r'\s{2,}\S+:\s', re.IGNORECASE)
MATCH_PLAYER = re.compile(r'NAME:\s+|\s+ID:\s+|\s+KILL:\s+', re.IGNORECASE)


Player = Tuple[str, str, int, int]


def define_team_size(file: TextIOWrapper) -> int:
    """Find out how much players in every team

    Parameters
    ----------
    file : TextIOWrapper
        Log file to be parsed

    Returns
    -------
    int
        Players in team

    """

    players = 0
    got_team = False

    for line in file.readlines():

        if line.startswith('TeamName'):

            if not got_team:
                got_team = True
            else:
                return players

        elif line.startswith('NAME') and got_team:

            players += 1

    raise ValueError("Could not figure out team size")


def process_team_line(line: str, team_size: int) -> List[str]:

    if team_size == 1:

        return re.findall(MATCH_DIGITS, line)

    else:

        team, *other = re.split(MATCH_TEAM, line)

        other = (re.sub(r'\D', '', x) for x in other)

        return [team.split(':')[-1].strip(), *other]


def process_player_line(line: str) -> List[str]:

    player = re.split(re.compile(r'\S+:\s'), line)

    return [re.sub(r'\W', '', x) for x in player[1:]]


def process_single_log_file(file: TextIOWrapper) -> Tuple[int, List[Player]]:
    """
    Parse tournament results and return list of players sorted by
    Teams and kills

    Return: Tuple with team size and list of parsed teams in it:
        List[Tuple[team_or_name, id, kills, killscore, rankscore, total_score]]
    """

    team_size = define_team_size(file)

    file.seek(0)

    table: List[Player] = []
    team: str = ""
    teams_dict: Dict[Player] = {}
    teams_list: List[Player] = []

    try:
        for index, line in enumerate(file.readlines(), start=1):

            if 'TeamName' in line:

                # TeamName, Rank, KillScore, RankScore, TotalScore
                # Cold Steel ['16', '10', '50', '60']
                # 24 ['0', '160', '160']

                if team_size == 1:
                    team_row = process_team_line(line, team_size)
                    team = f"Команда {team_row[0]}"
                else:
                    team, *team_row = process_team_line(line, team_size)
                    team_id = team_row[0]

            else:
                # ['BustㅤSavage', '415576113', '4']
                row = process_player_line(line)

                if row == []:
                    continue

                if team_size == 1:
                    teams_list.append(row + team_row[-3:])

                else:
                    if team_id in teams_dict:
                        # Add kills
                        teams_dict[team_id][2] += int(row[-1])
                    else:
                        # insert kills
                        team_row.insert(1, int(row[-1]))
                        teams_dict[team_id] = [team] + team_row

    except Exception as e:
        # Inject line which cause Exception to render it later in Django
        e.error_line = index
        e.filename = file.name
        raise

    table = teams_list if team_size == 1 else list(teams_dict.values())

    # Sort by kills
    table.sort(key=lambda x: (-int(x[-1]), -int(x[2])))

    return team_size, table


def process_multiple_files(*files: List[TextIOWrapper]) -> List[Player]:
    """
    Return list of players sorted by total kills
    """

    # {ID: [team, nickname, kills], ...}
    total = {}

    for file in files:

        team_size, result_list = process_single_log_file(file)

        # 'AVANG4R360': ['1076075937', '2', '40', '480', '520'],
        result_dict = {team[0]: team[1:] for team in result_list}

        # print(result_dict['Bust'])

        # ID is the key of results dict
    #     results = {item[2]: item for item in results_list}

        for team, team_result in result_dict.items():

            if team in total:

                team_id = team_result.pop(0)
                total[team] = [team_id] + [int(x) + int(y) for x, y in zip(total[team][1:], team_result)]

            else:
                total[team] = team_result

    total_list = [[k, *v] for k, v in total.items()]

    return team_size, sorted(total_list, key=lambda team: (-int(team[-1]), -int(team[2])))
