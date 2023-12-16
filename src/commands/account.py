from src.agents.user_service import UserGenerator, MakerConfig, generate_sample_agent
from src.providers.age import retrieve_age_provider
from src.providers.mail import retrieve_mail_provider
from src.providers.password import retrieve_password_provider
from src.providers.profile import retrieve_profile_provider
from typing import List


def generate_account(
        mail="f",
        nationality="r",
        gender=None,
        count=1,
        logging="pretty",
        password="r",
        password_length=20,
        age="r"
        ) -> List[dict]:
    
    mail_handler = retrieve_mail_provider(mail)
    profile_handler = retrieve_profile_provider(nationality, gender)
    password_handler = retrieve_password_provider(password, password_length)
    age_handler = retrieve_age_provider(age)

    generator = UserGenerator(
        MakerConfig(
            mail_generator = mail_handler,
            profile_generator = profile_handler,
            password_generator = password_handler,
            age_generator= age_handler
        )
    )

    agents = []
    for _ in range(int(count)):
        agent = generate_sample_agent(generator)
        agents.append(agent)

    agent_objects = [i.to_dict() for i in agents]
    

    if logging == "pretty":
        log = [i.to_json() for i in agents]
        for i in log:
            print(i)

    if logging == "output":
        print(agent_objects)
        

    return agent_objects
