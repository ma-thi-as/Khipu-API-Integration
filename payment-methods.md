## GET payments/{payment_id}

### Response:

#### Payment data:

- **payment_id** (String): Identificador único del pago, es una cadena alfanumérica de 12 caracteres. Cómo este identificador es único, se puede usar, por ejemplo, para evitar procesar una notificación repetida.
- **payment_url** (String): URL principal del pago, si el usuario no ha elegido previamente un método de pago se le muestran las opciones.
- **simplified_transfer_url** (String): URL de pago simplificado.
- **transfer_url** (String): URL de pago normal.
- **app_url** (String): URL para invocar el pago desde un dispositivo móvil usando la APP de Khipu.
- **ready_for_terminal** (Boolean): Es ‘true’ si el pago ya cuenta con todos los datos necesarios para abrir directamente la aplicación de pagos Khipu.
- **notification_token** (String): Cadena de caracteres alfanuméricos que identifican unicamente al pago, es el identificador que el servidor de Khipu enviará al servidor del comercio cuando notifique que un pago está conciliado.
- **receiver_id** (Long): Identificador único de una cuenta de cobro.
- **conciliation_date** (Date): Fecha y hora de conciliación del pago. Formato ISO-8601. Ej: 2017-03-01T13:00:00Z.
- **subject** (String): Motivo del pago.
- **amount** (Double).
- **currency** (String): El código de moneda en formato ISO-4217.
- **status** (String): Estado del pago, puede ser ‘pending’ (el pagador aún no comienza a pagar), ‘verifying’ (se está verificando el pago) o ‘done’, cuando el pago ya está confirmado.
- **status_detail** (String): Detalle del estado del pago.
- **body** (String): Detalle del cobro.
- **picture_url** (String): URL de cobro.
- **receipt_url** (String): URL del comprobante de pago.
- **return_url** (String): URL donde se redirige al pagador luego que termina el pago.
- **cancel_url** (String): URL donde se redirige al pagador luego de que desiste hacer el pago.
- **notify_url** (String): URL del webservice donde se notificará el pago.
- **notify_api_version** (String): Versión de la api de notificación.
- **expires_date** (Date): Fecha máxima para ejecutar el pago (en formato ISO-8601). El cliente podrá realizar varios intentos de pago hasta dicha fecha. Cada intento tiene un plazo individual de 3 horas para su ejecución.
- **attachment_urls** (Array[String]): URLs de archivos adjuntos al pago.

#### Payer data:

- **bank** (String): Nombre del banco seleccionado por el pagador.
- **bank_id** (String): Identificador del banco seleccionado por el pagador.
- **payer_name** (String): Nombre del pagador.
- **payer_email** (String): Correo electrónico del pagador.
- **personal_identifier** (String): Identificador personal del pagador.
- **bank_account_number** (String): Número de cuenta bancaria del pagador.
- **out_of_date_conciliation** (Boolean): Es ‘true’ si la conciliación del pago fue hecha luego de la fecha de expiración.
- **transaction_id** (String): Identificador del pago asignado por el cobrador.
- **custom** (String máximo 4096 caracteres): Campo genérico que asigna el cobrador al momento de hacer el pago.
- **responsible_user_email** (String): Correo electrónico de la persona responsable del pago.
- **send_reminders** (Boolean): Es ‘true’ cuando este es un cobro por correo electrónico y Khipu enviará recordatorios.
- **send_email** (Boolean): Es ‘true’ cuando Khipu enviará el cobro por correo electrónico.
- **payment_method** (String): Método de pago usado por el pagador, puede ser ‘regular_transfer’ (transferencia normal), ‘simplified_transfer’ (transferencia simplificada).
- **funds_source** (String): Origen de fondos usado por el pagador, puede ser ‘debit’ para pago con débito, ‘prepaid’ para pago con prepago, ‘credit’ para pago con crédito o vacío en el caso de que se haya pagado mediante transferencia bancaria.

#### Response Codes:

- **200:** Éxito
- **400:** Datos inválidos
- **403:** Error de autorización
- **503:** Error de operación
