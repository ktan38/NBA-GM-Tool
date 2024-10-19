class DraftPick:
    def __init__(self, year, round, current_team, origin_team=None, protections=None):
        """
        Represents a draft pick in the NBA.
        :param year: Year of the draft pick
        :param round: Round of the draft pick (1 or 2)
        :param current_team: The team that currently owns the draft pick
        :param origin_team: The team that originally owned the draft pick (if traded)
        :param protections: Protections attached to the pick (e.g., lottery protected, top-10 protected)
        """
        self.year = year
        self.round = round  # Either 1 or 2 (for round 1 or round 2)
        self.current_team = current_team
        self.origin_team = origin_team if origin_team else current_team  # Default to current team if no trade
        self.protections = protections if protections else {}

    # Getters
    def get_year(self):
        """Returns the draft year."""
        return self.year

    def get_round(self):
        """Returns the draft round (1 or 2)."""
        return self.round

    def get_current_team(self):
        """Returns the current team that holds the pick."""
        return self.current_team

    def get_origin_team(self):
        """Returns the team that originally owned the pick."""
        return self.origin_team

    def get_protections(self):
        """Returns the protections on the draft pick (if any)."""
        return self.protections

    # Setters
    def set_current_team(self, new_team):
        """
        Sets the new team that currently holds the pick (in case of a trade).
        :param new_team: The team that acquires the draft pick.
        """
        self.current_team = new_team

    def set_protections(self, new_protections):
        """
        Sets or updates protections on the draft pick.
        :param new_protections: A dictionary of new protections.
        """
        self.protections = new_protections

    def __repr__(self):
        """
        String representation of the draft pick, including origin team and protections.
        """
        round_str = f"Round {self.round}"
        protections_str = f"Protections: {self.protections}" if self.protections else "No protections"
        origin_str = f" (Traded from {self.origin_team})" if self.origin_team != self.current_team else ""
        return f"{self.year} {round_str} Pick owned by {self.current_team}{origin_str}, {protections_str}"
