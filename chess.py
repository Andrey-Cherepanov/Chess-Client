
class Rule:
    """Shows allowed moves for each piece type"""
    def __init__(self, rulestring):
        self.string = rulestring
        self.allowed = allowed_moves(rulestring)

    def allowed_moves(rulestring:String):
        pass

class Piece:
    def __init__(self, color, rules, position):
        self.color = color
        self.rules = rules
        self.position = position

    def move(self, move, game):
        """if rules allowes move, change position"""
        pass


def readrules(configs='rules.json'):
    """Read rules from config file
    standart path - 'rules.json'"""
    pass
