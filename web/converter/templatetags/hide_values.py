from typing import List

from django import template

register = template.Library()


@register.filter(name='hide_values')
def hide_values(player_row: List[str]) -> List[str]:
    """
    Pop hidden values from row with player's score

    Before:
        team_or_name, id, kills, killscore, rankscore, total_score
    After:
        team_or_name, kills, total_score
    """

    return [player_row[0], player_row[2], player_row[-1]]
