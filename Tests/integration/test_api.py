import pytest


@pytest.mark.integration
def test_user_3_has_10_posts(api_session, api_url):
    response = api_session.get(
        f"{api_url}/posts",
        params={"userId": 3}
    )

    assert response.status_code == 200
    assert len(response.json()) == 10


@pytest.mark.integration
def test_forecast_data_in_both_buckets(
        forecast_date,
        gcp_bucket,
        aws_bucket):

    assert forecast_date in gcp_bucket
    assert forecast_date in aws_bucket

    assert len(gcp_bucket[forecast_date]) > 0
    assert len(aws_bucket[forecast_date]) > 0