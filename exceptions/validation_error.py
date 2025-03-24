
class RaidNameNotRecognized(Exception):
    def __init__(self, raid):
        if raid is None:
            super().__init__("Invalid command syntax! The correct format is: !loot <raid>."
            " <raid> should be either 'icc25' for Icecrown Citadel-25 or 'rs25' for Ruby Sanctum-25.")
        else:
            super().__init__(f"{raid} is not a valid raid. Please type 'icc25' for Icecrown Citadel-25 or 'rs25' for Ruby Sanctum-25")

class InvalidRaidDate(ValueError):
    def __init__(self, date):
        super().__init__(f"Invalid date format: {date}. Please use YYYY-MM-DD.")

class EmptyDKPlist(Exception):
    def __init__(self):
        super().__init__("Not a single player with DKP was found. Please check if dkp points are on guild notes, "
        "backup your data on QDKP addon and try again")

class EmptyPlayerItemlist(Exception):
    def __init__(self, raid_name, raid_date):
        super().__init__(f"Loot was not found in the raid {raid_name}-({raid_date}). Please ensure that players buy gear directly through QDKP addon")
