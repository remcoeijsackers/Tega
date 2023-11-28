import click
from src.agents.namegen import Maker, MakerConfig, generate_sample_agent
from src.scraper import retrieve_disposable_mail, MailMonitor

@click.group()
def cli():
    """ Fake Agents for testing """

@cli.command('mail',  short_help='burner email')
@click.option("-i", "--inbox", type=bool, default=False, show_default="current user", help="also include a browsable inbox")
def mail(inbox):
    """ retrieve an burner email with optional inbox """
    if inbox:
        monitor= MailMonitor()
        print(monitor.check_mail())
    else:
        mail = retrieve_disposable_mail(False)
        print(mail)

@cli.command('account',  short_help='fake account')
@click.option("-f", "--format", type=str, show_default="current user", help="output format")
def account(format):
    mk = Maker(
        MakerConfig()
        )
    ag = generate_sample_agent(mk)
    if not format:
        print(ag.to_json())
    if format == "values":
        print(ag.to_json())

if __name__ == '__main__':
    cli()