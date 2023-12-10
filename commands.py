import click
from src.commands import generate_account

@click.group()
def cli():
    """ Fake accounts for testing """

@cli.command('account',  short_help='fake account')
@click.option("-m", "--mail", type=str, default="f", show_default="mail type [f]: fake", help="[f]ake/[b]urner: email type. include a burner mail [b] or a fake one [f]")
@click.option("-n", "--nationality", type=str, default="r", show_default="profile type [r]: random", help="[r]andom/<nationality>: profile type.  nationatily based = <Nationality>")
@click.option("-g", "--gender", type=str, default=None, show_default="gender type [None]: random",  help="[m]/[f]: gender of the profile" )
@click.option("-c", "--count", type=int, default=1, show_default=1, help="amount of accounts to generate")
@click.option("-l", "logging", type=str, default="pretty", show_default="[pretty]: log all accounts as they are created", help="[pretty]/[output]/[none]: logging options. output: log the output list of objects, pretty:log accounts as they are created, none: no logs.")
def account(mail, nationality, gender, count, logging):
    return generate_account(mail, nationality, gender, count, logging)

if __name__ == '__main__':
    cli()