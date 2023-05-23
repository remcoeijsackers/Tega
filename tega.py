import click
from src.agents.namegen import Maker, generate_sample_agent
from src.scraper import retrieve_disposable_mail
import datetime

@click.group()
def cli():
    pass

@cli.command()
def retrieve_mail():
    retrieve_disposable_mail()

@cli.command()
def generate_account():
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