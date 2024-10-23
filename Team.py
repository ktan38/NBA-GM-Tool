from enum import Enum
from . import PlayerManager, DraftPick
import requests
from basketball_reference_web_scraper.data import SalaryThresholds, TeamStatus

class Team:
    def __init__(self, name, player_manager, roster=None, payroll=0, cap_status=None):
        self.name = name
        self.roster = roster if roster else []
        self.payroll = payroll
        self.cap_status = cap_status
        self.player_manager = player_manager  # A reference to the player manager

    def add_player(self, player):
        if player not in self.roster:
            self.roster.append(player)
            print(f"Player {player.name} added to {self.name}.")
        else:
            print(f"Player {player.name} already in the roster.")

    def remove_player(self, player):
        if player in self.roster:
            self.roster.remove(player)
            print(f"Player {player.name} removed from {self.name}.")
        else:
            print(f"Player {player.name} is not in the roster.")

    def update_roster(self):
        """
        Updates the team's roster. This logic can be customized as needed.
        """
        print(f"Updating roster for {self.name}...")

    def update_payroll(self):
        """
        Updates the team's payroll based on player contracts. This logic can be customized as needed.
        """
        print(f"Updating payroll for {self.name}...")

    def display_team_info(self):
        print(f"Team: {self.name}")
        print(f"Payroll: {self.payroll}")
        print("Roster:")
        for player in self.roster:
            print(f"- {player.name}")