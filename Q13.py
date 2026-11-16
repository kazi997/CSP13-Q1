class SavingsAccount:
    def __init__(
        self,
        account_id: int,
        balance: float,
        previous_balance: float,
        annual_interest_rate: float,
    ):
        self.account_id = account_id
        self.balance = balance
        self.previous_balance = previous_balance
        self.annual_interest_rate = annual_interest_rate

    def set_interest_rate(self, updated_interest_rate: float) -> None:
        self.annual_interest_rate = updated_interest_rate

    def get_monthly_interest_rate(self) -> float:
        return self.annual_interest_rate / 12 / 100

    def get_monthly_interest(self) -> float:
        return self.balance * self.get_monthly_interest_rate()

    def get_balance_change_percent(self) -> float:
        if self.previous_balance == 0:
            raise ZeroDivisionError("Previous balance cannot be zero")
        return ((self.balance - self.previous_balance) / self.previous_balance) * 100

    def withdraw(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount


def cq() -> None:
    account = SavingsAccount(1122, 20_000.0, 18_500.0, 4.5)
    account.withdraw(2_500.0)
    account.deposit(3_000.0)

    print(f"Account id: {account.account_id}")
    print(f"Current Balance: {account.balance:.2f}")
    print(f"Monthly Interest Rate: {account.get_monthly_interest_rate() * 100:.3f}%")
    print(f"Monthly Interest: {account.get_monthly_interest():.2f}")
    print(f"Percentage change from previous balance: {account.get_balance_change_percent():.2f}%")


if __name__ == "__main__":
    cq()
