import pytest

import contextlib

from converter.load_logs import process_single_log_file, process_multiple_files


@pytest.mark.parametrize('filename, players_count, team_players', [
    ('1.log', 45, 1),
    ('2.log', 24, 2),
    ('4.log', 12, 4),
])
def test_single_file_converter(
        test_data_folder: str,
        filename: str,
        players_count: int,
        team_players: int):

    with open(test_data_folder / filename, 'r') as f:

        team_size, results = process_single_log_file(f)

        assert len(results) == players_count

        assert team_size == team_players

        prev_total_score: int = int(results[1][-1])
        prev_kills: int = int(results[1][2])

        for team in results[1:]:

            team_score = int(team[-1])

            team_kills = int(team[2])

            assert team_score <= prev_total_score

            if team_score == prev_total_score:

                assert team_kills <= prev_kills

            prev_total_score = team_score
            prev_kills = team_kills


def test_sorting_with_multiple_files(test_data_folder: str):

    with contextlib.ExitStack() as stack:

        filenames = [test_data_folder / f'multi{i}.log' for i in range(1, 3)]

        files = [stack.enter_context(open(fname, 'r')) for fname in filenames]

        team_size, results = process_multiple_files(*files)

        prev_team_total_score = int(results[0][-1])
        prev_team_kills = int(results[0][2])

        for team in results[1:]:

            team_total_score = int(team[-1])
            team_kills = int(team[2])

            assert team_total_score <= prev_team_total_score

            if team_total_score == prev_team_total_score:

                assert team_kills <= prev_team_kills

            prev_team_kills = team_kills
            prev_team_total_score = team_total_score
