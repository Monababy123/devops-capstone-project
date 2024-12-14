HEAD
name: CI Build
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    container: python:3.9-slim

   services:
  postgres:
    image: postgres:alpine
    ports:
      - 5432:5432
    env:
      POSTGRES_PASSWORD: pgs3cr3t
      POSTGRES_DB: testdb
    options: >-
      --health-cmd pg_isready
      --health-interval 10s  # Fixed, no quotes or colon
      --health-timeout 5s
      --health-retries 5


    steps:
      - name: Checkout
        uses: actions/checkout@v2
@app.route("/health")
def health():
    """Health Status"""
    return jsonify(dict(status="OK")), status.HTTP_200_OK
54ec043feaf31ad63f01165f234d912e900b9068

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip wheel
          pip install -r requirements.txt

HEAD
      - name: Lint with flake8
        run: |
          flake8 service --count --select=E9,F63,F7,F82 --show-source --statistics
          flake8 service --count --max-complexity=10 --max-line-length=127 --statistics

      - name: Run unit tests with nose
        run: nosetests
        env:
          DATABASE_URI: "postgresql://postgres:pgs3cr3t@postgres:5432/testdb"

@app.route("/")
def index():
    """Root URL response"""
    return (
        jsonify(
            name="Account REST API Service",
            version="1.0",
        ),
        status.HTTP_200_OK,
    )


@app.route("/accounts", methods=["POST"])
def create_accounts():
    """
    Creates an Account
    This endpoint will create an Account based on the data in the body that \
    is posted.
    """
    app.logger.info("Request to create an Account")
    check_content_type("application/json")
    account = Account()
    account.deserialize(request.get_json())
    account.create()
    message = account.serialize()
    location_url = url_for(
        "get_accounts", account_id=account.id, _external=True
    )
    location_url = "/"  # Remove once get_accounts has been implemented
    return make_response(
        jsonify(message), status.HTTP_201_CREATED, {"Location": location_url}
    )
54ec043feaf31ad63f01165f234d912e900b9068
