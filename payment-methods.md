# Payment Methods Documentation Please reference to API 2.0 DOC -> https://docs.khipu.com/openapi/es/v2/instant-payment/openapi/overview/

## Get Payment Details
Retrieve detailed information about a specific payment using its ID.

### Endpoint
```http
GET /payments/{payment_id}
```

### Response Structure

#### 🔐 Payment Core Information
| Field | Type | Description |
|-------|------|-------------|
| `payment_id` | String | Unique 12-character alphanumeric payment identifier. Used to prevent duplicate notification processing |
| `status` | String | Payment status: `pending`, `verifying`, or `done` |
| `status_detail` | String | Detailed payment status information |
| `amount` | Double | Payment amount |
| `currency` | String | Currency code in ISO-4217 format |
| `transaction_id` | String | Merchant-assigned payment identifier |

#### 🔗 Payment URLs
| Field | Type | Description |
|-------|------|-------------|
| `payment_url` | String | Main payment URL (shows payment options if method not selected) |
| `simplified_transfer_url` | String | Simplified payment process URL |
| `transfer_url` | String | Standard payment process URL |
| `app_url` | String | Mobile payment URL for Khipu APP |
| `receipt_url` | String | Payment receipt URL |
| `picture_url` | String | Payment image URL |

#### 📝 Payment Details
| Field | Type | Description |
|-------|------|-------------|
| `subject` | String | Payment reason |
| `body` | String | Detailed payment description |
| `custom` | String | Generic field set by merchant (max 4096 characters) |
| `notification_token` | String | Unique identifier for payment reconciliation notifications |
| `receiver_id` | Long | Unique collection account identifier |

#### 👤 Payer Information
| Field | Type | Description |
|-------|------|-------------|
| `payer_name` | String | Payer's full name |
| `payer_email` | String | Payer's email address |
| `personal_identifier` | String | Payer's personal identification |
| `responsible_user_email` | String | Email of person responsible for payment |

#### 🏦 Bank Details
| Field | Type | Description |
|-------|------|-------------|
| `bank` | String | Selected bank name |
| `bank_id` | String | Selected bank identifier |
| `bank_account_number` | String | Payer's bank account number |
| `payment_method` | String | Used payment method: `regular_transfer` or `simplified_transfer` |
| `funds_source` | String | Fund source: `debit`, `prepaid`, `credit`, or empty for bank transfer |

#### ⚙️ Configuration
| Field | Type | Description |
|-------|------|-------------|
| `ready_for_terminal` | Boolean | `true` if payment is ready for Khipu payment app |
| `send_reminders` | Boolean | `true` if Khipu should send payment reminders |
| `send_email` | Boolean | `true` if Khipu should send payment by email |
| `out_of_date_conciliation` | Boolean | `true` if payment reconciliation occurred after expiration |

#### 📅 Dates and Timeline
| Field | Type | Description |
|-------|------|-------------|
| `conciliation_date` | Date | Payment reconciliation date/time (ISO-8601) |
| `expires_date` | Date | Payment execution deadline (ISO-8601) |

#### 🔄 Callback URLs
| Field | Type | Description |
|-------|------|-------------|
| `return_url` | String | Redirect URL after successful payment |
| `cancel_url` | String | Redirect URL after payment cancellation |
| `notify_url` | String | Webhook URL for payment notifications |
| `notify_api_version` | String | Notification API version |

#### 📎 Additional Information
| Field | Type | Description |
|-------|------|-------------|
| `attachment_urls` | Array[String] | URLs of files attached to payment |

### Response Codes

| Code | Status | Description |
|------|--------|-------------|
| 200 | Success | Request processed successfully |
| 400 | Bad Request | Invalid data provided |
| 403 | Forbidden | Authorization error |
| 503 | Service Unavailable | Operation error |

### Important Notes

1. Payment attempts can be made multiple times until the expiration date
2. Each payment attempt has a 3-hour execution window
3. The notification token is used for server-to-server payment confirmation
4. Personal identifier and bank account information are only available for completed payments

### Example Response

```json
{
  "payment_id": "abc123def456",
  "status": "done",
  "amount": 1000.00,
  "currency": "CLP",
  "subject": "Product Purchase",
  "payer_name": "John Doe",
  "payment_method": "regular_transfer",
  "conciliation_date": "2024-03-01T13:00:00Z"
}
```
