# Plaid

## Overview

The Plaid Heron source is a combination of two distinct sources i.e. Plaid and Heron. 
Transactions retrieved from plaid are then passed to heron in order to get them categorised. 
The Plaid source supports Full Refresh syncs. It currently only supports pulling from the balances endpoint. 
It will soon support other data streams \(e.g. transactions\).

### Output schema

Output streams:

* [Balance](https://plaid.com/docs/api/products/#balance)
* [Transaction](https://plaid.com/docs/api/products/transactions/)
* [Category](https://docs.herondata.io/api#tag/Categories)

### Features

| Feature | Supported? |
| :--- | :--- |
| Full Refresh Sync | Yes |
| Incremental - Append Sync | Coming soon |
| Replicate Incremental Deletes | Coming soon |
| SSL connection | Yes |
| Namespaces | No |

## Getting started

### Requirements

* Plaid Account \(with client\_id and API key\)
* Access Token
* Heron Account (with username and password)

### Setup guide for Sandbox

This guide will walk through how to create the credentials you need to run this source in the sandbox of a new plaid account. For production use, consider using the Link functionality that Plaid provides [here](https://plaid.com/docs/api/tokens/#linktokencreate)

* **Create a Plaid account** Go to the [plaid website](https://plaid.com/) and click "Get API Keys". Follow the instructions to create an account.
* **Get Client id and API key** Go to the [keys page](https://dashboard.plaid.com/team/keys) where you will find the client id and your Sandbox API Key \(in the UI this key is just called "Sandbox"\).
* **Create an Access Token** First you have to create a public token key and then you can create an access token.
  * **Create public key** Make this API call described in [plaid docs](https://plaid.com/docs/api/sandbox/#sandboxpublic_tokencreate)

    ```bash
      curl --location --request POST 'https://sandbox.plaid.com/sandbox/public_token/create' \
          --header 'Content-Type: application/json;charset=UTF-16' \
          --data-raw '{
              "client_id": "<your-client-id>",
              "secret": "<your-sandbox-api-key>",
              "institution_id": "ins_43",
              "initial_products": ["auth", "transactions"]
          }'
    ```

  * **Exchange public key for access token** Make this API call described in [plaid docs](https://plaid.com/docs/api/tokens/#itempublic_tokenexchange). The public token used in this request, is the token returned in the response of the previous request. This request will return an `access_token`, which is the last field we need to generate for the config for this source!

    ```bash
    curl --location --request POST 'https://sandbox.plaid.com/item/public_token/exchange' \
      --header 'Content-Type: application/json;charset=UTF-16' \
      --data-raw '{
          "client_id": "<your-client-id>",
          "secret": "<your-sandbox-api-key>",
          "public_token": "<public-token-returned-by-previous-request>"
      }'
    ```
* **Create a Heron Account** Create username and password 
* We should now have everything we need to configure this source in the UI.

| Version | Date | Pull Request | Subject |
| :--- | :--- | :--- | :--- |

