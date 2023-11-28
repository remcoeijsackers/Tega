import click
from src.agents.namegen import Maker, MakerConfig, generate_sample_agent
from src.scraper import retrieve_disposable_mail, MailMonitor
from src.scraper.mail_generator import DisposableMail, FakeMail

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
@click.option("-m", "--mail", type=str, default="f", show_default="mail type", help="include a burner mail [b] or a fake one [f]")
def account(mail):
    if mail == "f":
        mail_handler = FakeMail()
    if mail == "b":
        mail_handler = DisposableMail()

    mk = Maker(
            MakerConfig(
                mail_generator = mail_handler
            )
        )
    ag = generate_sample_agent(mk)


    print(ag.to_json())

    return ag.to_json()

if __name__ == '__main__':
    cli()