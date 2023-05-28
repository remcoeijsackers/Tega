import click
from src.agents.namegen import Maker, MakerSettings, generate_sample_agent
from src.scraper import retrieve_disposable_mail, MailMonitor

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
    st = MakerSettings()
    mk = Maker(st)
    ag = generate_sample_agent(mk)
    ag.intro()
    
if __name__ == '__main__':
    cli()