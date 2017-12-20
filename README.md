# Timestamp Microservice

Microservice for fetching UNIX and Natural date information.

In fulfillment of the FreeCodeCamp's [Backend Certification](https://github.com/freeCodeCamp/freeCodeCamp#3-back-end-certification). Specs listed [here](https://www.freecodecamp.org/challenges/timestamp-microservice)

## Usage

1. Send a `GET` request to the either of the following routes:

```
/<int:timestamp_unix> - A valid UNIX timestamp ex. 5233351251
/<timestamp_natural> - A Natural Language date ex. 'June 5, 1996'
```

2. Receive a JSON response

```json
// GET /5233351251
{
    "natural": "November 03, 2135",
    "unix": 5233351251
}

// GET /June%205,%201996
{
    "natural": "June 05, 1996",
    "unix": 833932800
}

// GET /foobar
{
    "natural": null,
    "unix": null
}
```

## License

See the [license file](LICENSE) for more information.