import pytest
import requests


@pytest.fixture
def api_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def api_session():
    session = requests.Session()
    yield session
    session.close()


@pytest.fixture
def forecast_date():
    return "2026-10-01"


@pytest.fixture
def gcp_bucket(forecast_date):
    return {
        forecast_date: ["forecast_data.csv"]
    }


@pytest.fixture
def aws_bucket(forecast_date):
    return {
        forecast_date: ["forecast_data.csv"]
    }