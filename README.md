# Khipu Payment API Integration

A Python-based asynchronous client for integrating with Khipu's payment processing API. This implementation provides a robust interface for managing payments, bank information, and transaction flows using Khipu's API v2.0.

## Features

- 🏦 Bank information retrieval
- 💰 Payment creation and management
- 🔒 Secure authentication handling
- ⚡ Asynchronous request processing
- 🔄 Transaction lifecycle management

## Prerequisites

- Python 3.7+
- `aiohttp` library
- Valid Khipu API credentials (receiver_id and secret)

## Installation

```bash
pip install aiohttp
```

## Configuration

Create a credentials dictionary with your Khipu API credentials:

```python
credentials = {
    'receiver_id': 'your_receiver_id',
    'secret': 'your_secret_key'
}
```

## Usage

### Get Available Banks

Retrieve a list of available banks for payment processing:

```python
banks = get_available_banks()
```

### Create a Payment

Create a new payment with required parameters:

```python
payment_params = {
    "amount": "1000",
    "currency": "CLP",
    "subject": "Product Purchase",
    "transaction_id": "unique_transaction_id"
}

payment_response = make_payment(payment_params)
```

Optional parameters can be included:
```python
payment_params = {
    "amount": "1000",
    "currency": "CLP",
    "subject": "Product Purchase",
    "transaction_id": "unique_transaction_id",
    "notify": "https://your-callback-url.com",
    "notify_api_version": "1.3"
}
```

### Manage Payments

Check payment status:
```python
status = get_payment_by_id("payment_id")
```

Delete a payment:
```python
result = delete_payment("payment_id")
```

Confirm a payment:
```python
confirmation = confirm_payment(payment_id)
```

## Authentication

The library handles authentication automatically using HMAC-SHA256:

- GET/DELETE requests: Signs the method and URL
- POST requests: Signs the method, URL, and sorted parameters
- All requests include the receiver_id and generated hash in the Authorization header

## Security Features

- URL encoding for special characters
- Parameter sorting for consistent signatures
- Case-insensitive parameter handling
- Required parameter validation
- Secure hash generation using HMAC-SHA256

## Error Handling

The library includes validation for:
- Required parameters presence
- Parameter formatting
- API response handling

## License

This project is licensed under the MIT License - see the LICENSE file for details.
