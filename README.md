# Django BoostNet OCPP App

A reusable django app based on [Levity](https://github.dev/keeth/levity)
This contains the Levity backend, powered by Django (WSGI, synchronous workers)

This must be connected to a AMQP message broker (eg rabbitmq) to consume events for the backend.

## settings.py Variables

### `AMQP_URL`

Eg:

```python
AMQP_URL = os.environ.get(
    "AMQP_URL",
    "amqp://guest:guest@localhost:5672/%2F?connection_attempts=20&retry_delay=1",
)
```

### `OCPP_HEARTBEAT_INTERVAL`

```python
OCPP_HEARTBEAT_INTERVAL = 3600
```

### `OCPP_MIDDLEWARE`

```python
# Following is the default middleware config
# No need to set again
# Can leave as not-set
OCPP_MIDDLEWARE = {
    (Action.Authorize, MessageType.call): [AuthorizeMiddleware],
    (Action.BootNotification, MessageType.call): [BootNotificationMiddleware],
    (Action.DataTransfer, MessageType.call): [DataTransferMiddleware],
    (Action.DiagnosticsStatusNotification, MessageType.call): [
        DiagnosticsStatusNotificationMiddleware
    ],
    (Action.FirmwareStatusNotification, MessageType.call): [
        FirmwareStatusNotificationMiddleware
    ],
    (Action.Heartbeat, MessageType.call): [HeartbeatMiddleware],
    (Action.MeterValues, MessageType.call): [MeterValuesMiddleware],
    (Action.StartTransaction, MessageType.call): [
        OrphanedTransactionMiddleware,
        StartTransactionMiddleware,
    ],
    (Action.StatusNotification, MessageType.call): [
        AutoRemoteStartMiddleware, # This is the additional middleware added (see default configuration)
        StatusNotificationMiddleware,
    ],
    (Action.StopTransaction, MessageType.call): [StopTransactionMiddleware],
}
```

## Start services

```shell
python manage.py runserver & # Normal server
python manage.py consume_rpc_queue & # Consume RPC commands (this app)
```

## Simulator

This packages a simulator UI. Include the app urls to use it.

````python
urlpatterns += [
    path("demo/ocpp/", include("ocpp.urls"), name="ocpp_demo"),
]
```

## Default configuration

By default, when a charge point goes into the _Preparing_ state, a _RemoteStartTransaction_ message will be automatically sent to it.

## RPC

Using this django app, the websocket server can be decoupled from the main backend server. This has several benefits:

- The websocket service can be deployed and scaled independently.
- The websocket service can be deployed at the edge, close to the charge points, if necessary.
- The backend service is greatly simplified - it's standard WSGI Django which is simpler to develop and test than ASGI and channels.

RabbitMQ is used as the RPC layer connecting **backend (which has this django app installed)** and **websocket service (ws)**. When a **ws** service starts up, it creates an ephemeral reply channel. Multiple **ws** services can be deployed independently. Each **ws** service communicates with the **backend** server, which implements the OCPP protocol and contains all business logic.

# State of the project

See [Levity project status](https://github.com/keeth/levity#state-of-the-project).
This is a helper app to be used by BoostNet chargers.

## Features

- Partial OCPP 1.6j support - Levity/BoostNet does not strive to be a complete reference implementation of OCPP, we are focused on solving practical EVSE management needs. This django app implements some more features as required by BoostNet.
- Charge points, transactions, meter values, and OCPP messages are modeled and persisted by the system.
- Middleware-style approach to extensibility (see auto_remote_start.py for an example)
- Tested with the Grizzl-E Smart charger
- Satisfies the OCPP 1.6j requirement for synchronicity - each charge point is allocated a separate "call queue" which ensures that this project will wait for a response to a CALL message before sending another CALL message.

## Grizzl-E Smart bug workarounds

The Grizzl-E Smart charger has several bugs in the current firmware (0.5) which are worked around by Levity:

- Websocket ping/pong is disabled, due to Grizzl-E sometimes sending invalid pongs, causing disconnection.
- The OCPP websocket protocol header is not required, because Grizzl-E does not send one.
````
