import click
from src.agents.namegen import Maker, generate_sample_agent
from src.scraper import retrieve_disposable_mail, MailMonitor
import datetime

@click.group()
def cli():
    """ Fake Agents for testing """

@cli.command('mail',  short_help='burner email')
@click.option("-i", "--inbox", type=bool, default=False, show_default="current user", help="also include a browsable inbox")
def mail(inbox):
    """ retrieve an burner email with optional inbox """
    if inbox:
        x= MailMonitor()
        print(x.check_mail())
    else:
        retrieve_disposable_mail()

@cli.command('account',  short_help='fake account')
def account():
    ag = generate_sample_agent()
    print(ag.name())
    print(ag.nat)
    x = datetime.datetime.now().date() - ag.age.date()
    yold = x/365
    print(f"{ag.age.date()} ({yold.days})")
    print(ag.email)
    print(ag.password)
    print("\n")
    
if __name__ == '__main__':
    cli()