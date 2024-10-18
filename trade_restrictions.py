



class NBATradeRestrictions:
    # Salary thresholds for 2023-2024 season (approximate values)
    SALARY_CAP = 136_000_000  # Soft cap
    LUXURY_TAX_LINE = 165_000_000  # Luxury tax threshold
    FIRST_APRON = 172_000_000  # First apron
    SECOND_APRON = 182_500_000  # Second apron

    # Exceptions
    NON_TAXPAYER_MLE = 12_400_000  # Non-Taxpayer Mid-Level Exception
    TAXPAYER_MLE = 5_000_000  # Taxpayer Mid-Level Exception
    BAE = 4_000_000  # Bi-Annual Exception
    ROOM_EXCEPTION = 7_700_000  # Room Exception
    MINIMUM_SALARY = 1_000_000  # Approx. value, varies by player experience

    def __init__(self, team_name, payroll, has_used_bae_last_year=False):
        self.team_name = team_name
        self.payroll = payroll
        self.has_used_bae_last_year = has_used_bae_last_year  # Tracks if BAE was used last season
    
    def get_status(self):
        """Determines the current financial status of the team based on its payroll."""
        if self.payroll < self.SALARY_CAP:
            return "Under the Cap"
        elif self.SALARY_CAP <= self.payroll < self.LUXURY_TAX_LINE:
            return "Over the Cap, Under Luxury Tax Line"
        elif self.LUXURY_TAX_LINE <= self.payroll < self.FIRST_APRON:
            return "Luxury Tax Payer, Under First Apron"
        elif self.FIRST_APRON <= self.payroll < self.SECOND_APRON:
            return "Over First Apron, Under Second Apron"
        else:
            return "Over Second Apron"
    
    def trade_limitations(self):
        """Returns a list of trade restrictions based on the team's payroll."""
        status = self.get_status()
        
        if status == "Under the Cap":
            return [
                "Can take back up to 125% of outgoing salary in trades.",
                "Can sign free agents with cap space.",
                "Can use the Room Exception ($7.7 million)."
            ]
        elif status == "Over the Cap, Under Luxury Tax Line":
            return [
                "Can use Non-Taxpayer Mid-Level Exception (about $12.4 million).",
                "Can use Bi-Annual Exception (about $4 million).",
                "Can sign and trade players.",
                "Can take back up to 125% + $100,000 of outgoing salary in trades."
            ]
        elif status == "Luxury Tax Payer, Under First Apron":
            return [
                "Can use Taxpayer Mid-Level Exception (about $5 million).",
                "Cannot use the Bi-Annual Exception.",
                "Can take back up to 125% + $100,000 of outgoing salary in trades."
            ]
        elif status == "Over First Apron, Under Second Apron":
            return [
                "Cannot use the Taxpayer Mid-Level Exception.",
                "Cannot use sign-and-trade transactions to acquire players.",
                "Limited to taking back 110% of outgoing salary in trades."
            ]
        elif status == "Over Second Apron":
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
        
        if status == "Under the Cap":
            return [
                f"Room Exception: ${self.ROOM_EXCEPTION:,}",
                "Can sign free agents using cap space."
            ]
        elif status == "Over the Cap, Under Luxury Tax Line":
            exceptions = [
                f"Non-Taxpayer Mid-Level Exception: ${self.NON_TAXPAYER_MLE:,}",
            ]
            if not self.has_used_bae_last_year:
                exceptions.append(f"Bi-Annual Exception: ${self.BAE:,}")
            return exceptions
        elif status == "Luxury Tax Payer, Under First Apron":
            return [
                f"Taxpayer Mid-Level Exception: ${self.TAXPAYER_MLE:,}",
            ]
        elif status == "Over First Apron, Under Second Apron":
            return [
                "Cannot use the Taxpayer Mid-Level Exception."
            ]
        elif status == "Over Second Apron":
            return [
                "No exceptions available (cannot use any MLE or Bi-Annual Exception)."
            ]
    
    def display_restrictions(self):
        """Display the team's current payroll status, trade limitations, and available exceptions."""
        print(f"Team: {self.team_name}")
        print(f"Payroll: ${self.payroll:,}")
        print(f"Status: {self.get_status()}")
        print("Trade Limitations:")
        for restriction in self.trade_limitations():
            print(f"- {restriction}")
        print("\nAvailable Exceptions:")
        for exception in self.available_exceptions():
            print(f"- {exception}")

# Example usage:
team_a = NBATradeRestrictions("Team A", 180_000_000, has_used_bae_last_year=False)  # Example team with payroll of $180M
team_a.display_restrictions()

team_b = NBATradeRestrictions("Team B", 140_000_000, has_used_bae_last_year=True)  # Example team with payroll of $140M, used BAE last season
team_b.display_restrictions()