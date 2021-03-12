import pytest

import contextlib

from converter.load_logs import process_single_log_file, process_multiple_files


@pytest.mark.parametrize('filename, players_count, team_players', [
    ('1.log', 45, 1),
    ('2.log', 47, 2),
    ('4.log', 48, 4),
])
def test_single_file_converter(
        test_data_folder: str,
        filename: str,
        players_count: int,
        team_players: int):

    with open(test_data_folder / filename, 'r') as f:

        results = process_single_log_file(f)

        assert len(results) == players_count

        first_team = results[0][0]

        players_in_team = 0

        for player in results:

            if player[0] != first_team:
                break
            players_in_team += 1

        assert players_in_team == team_players


def test_process_multiple_files(test_data_folder: str):

    with contextlib.ExitStack() as stack:

        filenames = [test_data_folder / f'multi{i}.log' for i in range(1, 3)]

        files = [stack.enter_context(open(fname, 'r')) for fname in filenames]

        results = process_multiple_files(*files)

        prev = results[0][-1]

        for player in results[1:]:

            assert player[-1] <= prev
            prev = player[-1]
