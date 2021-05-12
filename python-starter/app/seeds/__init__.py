from flask.cli import AppGroup
from .users import seed_users, undo_users, seed_currencies, undo_currencies, seed_posts, undo_posts, seed_trades, undo_trades, seed_userBalance, undo_userBalance

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_currencies()
    seed_posts()
    seed_trades()
    seed_userBalance()
    # Add other seed functions here

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_currencies()
    #! the undo's below aren't required as cascades from users tables clears it out
    # undo_posts()
    # undo_trades()
    # undo_userBalance()
    # Add other undo functions here
