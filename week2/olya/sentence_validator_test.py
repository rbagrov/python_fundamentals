from faker import Faker
from week2.olya.sentence_validator import sentence_validator


def test_sentence_validator():
    fake = Faker()
    output = sentence_validator(fake.text())
    assert output is True


