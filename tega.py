from flask import jsonify
from flask import request
from flask.cli import AppGroup
import click

from src.application import app as flask_app
from src.commands import generate_account
from src.commands.request_handler import flaskAccountHandler

from src.commands import generate_account
from src.commands.command_handler import CliAccountHandler

account_cli = AppGroup('account-group', help="help")

@account_cli.command('create_accounts',  short_help='fake accounts cli')
@click.option("-m", "--mail", type=str, default="f", show_default="mail type [f]: fake", help="[f]ake/[b]urner: email type. include a burner mail [b] or a fake one [f]")
@click.option("-n", "--nationality", type=str, default="r", show_default="profile type [r]: random", help="[r]andom/<nationality>: profile type.  nationatily based = <Nationality>")
@click.option("-g", "--gender", type=str, default=None, show_default="gender type [None]: random",  help="[m]/[f]: gender of the profile" )
@click.option("-c", "--count", type=int, default=1, show_default=1, help="amount of accounts to generate")
@click.option("-l", "logging", type=str, default="pretty", show_default="[pretty]: log all accounts as they are created", help="[pretty]/[output]/[none]: logging options. output: log the output list of objects, pretty:log accounts as they are created, none: no logs.")
def create_accounts(mail, nationality, gender, count, logging):
    handler = CliAccountHandler
    args = {"mail": mail, "nationality": nationality, "gender": gender, "count": count, "logging": logging}
    config = handler.handle_request(args)
    users = generate_account(
         **config
        )
    print(users)
    return users


@flask_app.route("/")
def account():
    handler = flaskAccountHandler

    config = handler.handle_request(args=request.args)
    users = generate_account(
         **config
        )
    response_data = {
         "config": config,
         "accounts": users
    }

    return jsonify(response_data)

flask_app.cli.add_command(account_cli)

if __name__ == '__main__':
    flask_app.cli()