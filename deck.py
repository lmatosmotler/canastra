import numpy as np


class Game:
    
def get_card_value(
        card: str
    ) -> int:
    """
    Get the value of a card following canastra rules.
    
    Parameters
    ----------
    card: int
        The whose value the user wants to know.

    Returns
    -------
    int
        The card value.
    """
    low_values = ["3","4","5","6","7"]
    medium_values = ["8","9","d","j","q","k"]
    high_values = ["2","c"]
    
    if card[0] in low_values:
        return 5
    elif card[0] in medium_values:
        return 10
    elif card[0] in high_values:
        return 20
    else:
        return 15

def get_hand_value(
        cards_on_hand: List[str]
    ) -> int:
    """
    Compute the total value of the cards on hand.
    """

