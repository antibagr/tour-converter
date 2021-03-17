import os
from pathlib import Path

from web.converter.load_logs import define_team_size, process_single_log_file


root = Path(__file__).resolve().parent / 'web' / 'tests' / 'data'

dirs = [root / 'solo', root / 'duo', root / 'squad']

for directory in dirs:

    print()
    print(f"{str(directory):-^168}")
    print()

    for file in os.listdir(directory):

        print()
        print(f"{str(file): ^168}")
        print()

        with open(directory / file, 'r') as f:
            result = process_single_log_file(f)

        print(result)
#
#
# with contextlib.ExitStack() as stack:
#
#     filenames = [test_data_folder / f'multi{i}.log' for i in range(1, 3)]
#
#     files = [stack.enter_context(open(fname, 'r')) for fname in filenames]
#
#     results = process_multiple_files(*files)

# import re
# import itertools
#
# regex = re.compile(r'(TeamName:)(.+)', re.IGNORECASE)
#
# def render(line: str) -> list:
#     x = [re.split(r'[\n\r\s{2,}]+', x) for x in trg_str.split(':')]
#
#     return list(filter(lambda x: x != '', itertools.chain(*x)))


# print(regex.findall(trg_str))
