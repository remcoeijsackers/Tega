import click
from src.agents.user_service import UserGenerator, MakerConfig, generate_sample_agent
from src.providers.mail import retrieve_mail_provider
from src.providers.profile import retrieve_profile_provider
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
@click.option("-m", "--mail", type=str, default="f", show_default="mail type", help="include a burner mail [b] or a fake one [f]")
@click.option("-p", "--profile", type=str, default="n", show_default="profile type", help="profile type")
def account(mail, profile):
    
    mail_handler = retrieve_mail_provider(mail)
    profile_handler = retrieve_profile_provider(profile)

    generator = UserGenerator(
        MakerConfig(
            mail_generator = mail_handler,
            profile_generator=profile_handler

        )
    )

    agent = generate_sample_agent(generator)


    print(agent.to_json())

    return agent.to_json()

if __name__ == '__main__':
    cli()