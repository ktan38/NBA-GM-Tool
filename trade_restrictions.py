from basketball_reference_web_scraper.data import OutputType, Team, SalaryThresholds, TradeExceptions, TeamStatus, TEAM_TO_TEAM_ABBREVIATION

from basketball_reference_web_scraper.html import SalariesPage

from basketball_reference_web_scraper.http_service import HTTPService





class NBATradeRestrictions:

    def __init__(self, team_name, payroll, has_used_bae_last_year=False):
        self.team_name = team_name


        self.payroll = payroll
        self.has_used_bae_last_year = has_used_bae_last_year  # Tracks if BAE was used last season
        
        self.SALARY_CAP = SalaryThresholds.SALARY_CAP.value
        self.LUXURY_TAX = SalaryThresholds.LUXURY_TAX.value
        self.FIRST_APRON = SalaryThresholds.FIRST_APRON.value
        self.SECOND_APRON = SalaryThresholds.SECOND_APRON.value

        self.NON_TAXPAYER_MLE = TradeExceptions.NON_TAXPAYER_MLE.value
        self.TAXPAYER_MLE = TradeExceptions.TAXPAYER_MLE.value
        self.BAE = TradeExceptions.BAE.value
        self.ROOM_EXCEPTION = TradeExceptions.ROOM_EXCEPTION.value
        self.MINIMUM_SALARY = TradeExceptions.MINIMUM_SALARY.value

    def get_status(self):
        """Determines the current financial status of the team based on its payroll."""
        if self.payroll < self.SALARY_CAP:
            return TeamStatus.UNDER_THE_CAP
        elif self.SALARY_CAP <= self.payroll < self.LUXURY_TAX:
            return TeamStatus.OVER_THE_CAP_UNDER_LUXURY_TAX
        elif self.LUXURY_TAX <= self.payroll < self.FIRST_APRON:
            return TeamStatus.LUXURY_TAX_PAYER
        elif self.FIRST_APRON <= self.payroll < self.SECOND_APRON:
            return TeamStatus.OVER_FIRST_APRON
        else:
            return TeamStatus.OVER_SECOND_APRON

    def trade_limitations(self):
        """Returns a list of trade restrictions based on the team's payroll."""
        status = self.get_status()

        if status == TeamStatus.UNDER_THE_CAP:
            return [
                "Can take back up to 125% of outgoing salary in trades.",
                "Can sign free agents with cap space.",
                "Can use the Room Exception ($7.7 million)."
            ]
        elif status == TeamStatus.OVER_THE_CAP_UNDER_LUXURY_TAX:
            return [
                "Can use Non-Taxpayer Mid-Level Exception (about $12.4 million).",
                "Can use Bi-Annual Exception (about $4 million).",
                "Can sign and trade players.",
                "Can take back up to 125% + $100,000 of outgoing salary in trades."
            ]
        elif status == TeamStatus.LUXURY_TAX_PAYER:
            return [
                "Can use Taxpayer Mid-Level Exception (about $5 million).",
                "Cannot use the Bi-Annual Exception.",
                "Can take back up to 125% + $100,000 of outgoing salary in trades."
            ]
        elif status == TeamStatus.OVER_FIRST_APRON:
            return [
                "Cannot use the Taxpayer Mid-Level Exception.",
                "Cannot use sign-and-trade transactions to acquire players.",
                "Limited to taking back 110% of outgoing salary in trades."
            ]
        elif status == TeamStatus.OVER_SECOND_APRON:
            return [
                "Cannot aggregate salaries in trades (can't combine multiple players to match a bigger contract).",
                "Cannot trade future first-round picks more than 6 years out.",
                "Cannot sign buyout players if it takes them further over the apron.",
                "Cannot use the Mid-Level Exception or Bi-Annual Exception.",
                "Limited to taking back 110% of outgoing salary in trades."
            ]

    def available_exceptions(self):
        """Determines what salary cap exceptions are available to the team."""
        status = self.get_status()

        if status == TeamStatus.UNDER_THE_CAP:
            return [
                f"Room Exception: ${self.ROOM_EXCEPTION:,}",
                "Can sign free agents using cap space."
            ]
        elif status == TeamStatus.OVER_THE_CAP_UNDER_LUXURY_TAX:
            exceptions = [
                f"Non-Taxpayer Mid-Level Exception: ${self.NON_TAXPAYER_MLE:,}",
            ]
            if not self.has_used_bae_last_year:
                exceptions.append(f"Bi-Annual Exception: ${self.BAE:,}")
            return exceptions
        elif status == TeamStatus.LUXURY_TAX_PAYER:
            return [
                f"Taxpayer Mid-Level Exception: ${self.TAXPAYER_MLE:,}",
            ]
        elif status == TeamStatus.OVER_FIRST_APRON:
            return [
                "Cannot use the Taxpayer Mid-Level Exception."
            ]
        elif status == TeamStatus.OVER_SECOND_APRON:
            return [
                "No exceptions available (cannot use any MLE or Bi-Annual Exception)."
            ]

    def display_restrictions(self):
        """Display the team's current payroll status, trade limitations, and available exceptions."""
        print(f"Team: {self.team_name}")
        print(f"Payroll: ${self.payroll:,}")
        print(f"Status: {self.get_status().value}")
        print("Trade Limitations:")
        for restriction in self.trade_limitations():
            print(f"- {restriction}")
        print("\nAvailable Exceptions:")
        for exception in self.available_exceptions():
            print(f"- {exception}")

# Example usage:
team_a = NBATradeRestrictions(Team.MIAMI_HEAT, 180_000_000, has_used_bae_last_year=False)  # Example team with payroll of $180M
team_a.display_restrictions()

team_b = NBATradeRestrictions(Team.MIAMI_HEAT, 140_000_000, has_used_bae_last_year=True)  # Example team with payroll of $140M, used BAE last season
team_b.display_restrictions()